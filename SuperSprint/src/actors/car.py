from math import atan2, degrees, hypot
from lib.actor import Actor, Arena, Point
from lib.polar import coterminal, move_around

class Car(Actor):
    """Classe base per una vettura da corsa in Super Sprint."""
    def __init__(self, pos: Point, color: int = 0, name: str = "Car"):
        self._pos = (float(pos[0]), float(pos[1]))
        self._prev_pos = self._pos
        self._color = color % 4
        self._name = name
        self._size = (16, 16)

        # Parametri fisici
        self._speed = 0.0
        self._max_speed = 4.2
        self._acceleration = 0.16
        self._friction = 0.04
        self._brake_force = 0.22
        self._max_reverse = -1.4
        self._angle = 0.0  # 0° = destra, 90° = giù, 180° = sinistra, 270° = su
        self._prev_angle = self._angle
        self._turn_rate = 6.0

        # Stato di gara
        self._target_cp_idx = 0
        self._laps = 0
        self._total_cps_hit = 0
        self._is_finished = False
        self._finish_rank = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def color(self) -> int:
        return self._color

    @property
    def speed(self) -> float:
        return self._speed

    @property
    def angle(self) -> float:
        return self._angle

    @property
    def laps(self) -> int:
        return self._laps

    @property
    def target_checkpoint_index(self) -> int:
        return self._target_cp_idx

    @property
    def total_checkpoints_hit(self) -> int:
        return self._total_cps_hit

    @property
    def is_finished(self) -> bool:
        return self._is_finished

    @property
    def finish_rank(self) -> int:
        return self._finish_rank

    def set_finish(self, rank: int):
        self._is_finished = True
        self._finish_rank = rank
        self._speed = 0.0

    @property
    def center(self) -> Point:
        return (self._pos[0] + self._size[0] / 2.0, self._pos[1] + self._size[1] / 2.0)

    def pos(self) -> Point:
        return self._pos

    def size(self) -> Point:
        return self._size

    def sprite(self) -> tuple[str, Point, Point]:
        """
        Calcola l'area di ritaglio esatta (16x16) nello spritesheet super-sprint.png
        per il colore dell'auto e i 32 angoli di rotazione.
        """
        # Lo spritesheet ruota in senso antiorario; l'angolo cartesiano ruota in senso orario
        sprite_angle = (360.0 - (self._angle % 360.0)) % 360.0
        # 360° / 32 frame = 11.25° per frame. Moltiplicare per 4/45 equivale a dividere per 11.25
        dir_index = int((sprite_angle + 5.625) // 11.25) % 32

        dir_col = dir_index % 8
        dir_row = dir_index // 8

        color_x_block = self._color % 2
        color_y_block = self._color // 2

        clip_x = (color_x_block * 8 + dir_col) * 16
        clip_y = (color_y_block * 4 + dir_row) * 16

        return ("super-sprint.png", (clip_x, clip_y), self._size)

    def advance_checkpoint(self, total_checkpoints: int):
        """Avanza al prossimo checkpoint atteso. Se completa un giro, incrementa laps."""
        self._total_cps_hit += 1
        self._target_cp_idx = (self._target_cp_idx + 1) % total_checkpoints
        if self._target_cp_idx == 0:
            self._laps += 1

    def bounce_back(self, dampening: float = 0.35):
        """Fa rimbalzare l'auto all'indietro a seguito di un impatto con un muro."""
        self._pos = self._prev_pos
        self._speed = -self._speed * dampening

    def move(self, arena: Arena):
        """Metodo astratto implementato da UserCar e CpuCar."""
        raise NotImplementedError("Implementato nelle sottoclassi")


class UserCar(Car):
    """Auto controllata da un giocatore umano da tastiera."""
    def __init__(self, pos: Point, color: int = 0, name: str = "Player 1",
                 controls: dict = None):
        super().__init__(pos, color, name)
        self._controls = controls or {
            "up": "ArrowUp",
            "down": "ArrowDown",
            "left": "ArrowLeft",
            "right": "ArrowRight"
        }

    def move(self, arena: Arena):
        self._prev_pos = self._pos
        self._prev_angle = self._angle

        if self._is_finished:
            return

        keys = arena.current_keys()

        # Accelerazione e frenata
        accelerating = self._controls["up"] in keys
        braking = self._controls["down"] in keys
        turning_left = self._controls["left"] in keys
        turning_right = self._controls["right"] in keys

        if accelerating:
            self._speed = min(self._speed + self._acceleration, self._max_speed)
        elif braking:
            self._speed = max(self._speed - self._brake_force, self._max_reverse)
        else:
            # Attrito naturale
            if self._speed > 0:
                self._speed = max(0.0, self._speed - self._friction)
            elif self._speed < 0:
                self._speed = min(0.0, self._speed + self._friction)

        # Sterzata (più reattiva se l'auto è in movimento, ma possibile anche a bassa velocità)
        if abs(self._speed) > 0.05:
            turn_mult = 1.0 if self._speed >= 0 else -1.0
            if turning_left:
                self._angle = (self._angle - self._turn_rate * turn_mult) % 360.0
            if turning_right:
                self._angle = (self._angle + self._turn_rate * turn_mult) % 360.0

        # Aggiornamento posizione polare
        if abs(self._speed) > 0.001:
            self._pos = move_around(self._pos, self._speed, self._angle)


class CpuCar(Car):
    """Auto controllata dall'intelligenza artificiale che naviga i checkpoint."""
    def __init__(self, pos: Point, color: int = 1, name: str = "CPU 1",
                 checkpoint_manager = None, difficulty: float = 1.0):
        super().__init__(pos, color, name)
        self._cp_manager = checkpoint_manager
        # Difficoltà influenza la velocità massima e la reattività
        self._max_speed = 3.6 + 0.5 * difficulty
        self._turn_rate = 5.5 + 1.2 * difficulty
        self._acceleration = 0.14

    def move(self, arena: Arena):
        self._prev_pos = self._pos
        self._prev_angle = self._angle

        if self._is_finished:
            return

        if not self._cp_manager:
            return

        # Target attuale
        target_cp = self._cp_manager.get_checkpoint(self._target_cp_idx)
        cx, cy = self.center
        dx = target_cp.x - cx
        dy = target_cp.y - cy

        # Angolo ideale verso il checkpoint
        desired_angle = degrees(atan2(dy, dx)) % 360.0
        angle_diff = coterminal(desired_angle - self._angle)

        # Sterzata fluida verso l'angolo ideale
        turn_step = max(-self._turn_rate, min(self._turn_rate, angle_diff))
        self._angle = (self._angle + turn_step) % 360.0

        # Modulazione velocità: rallenta leggermente nelle curve strette
        abs_diff = abs(angle_diff)
        if abs_diff > 45.0:
            target_speed = self._max_speed * 0.65
        elif abs_diff > 25.0:
            target_speed = self._max_speed * 0.85
        else:
            target_speed = self._max_speed

        if self._speed < target_speed:
            self._speed = min(self._speed + self._acceleration, target_speed)
        else:
            self._speed = max(target_speed, self._speed - self._friction)

        # Avanzamento
        self._pos = move_around(self._pos, self._speed, self._angle)
