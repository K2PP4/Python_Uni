from math import dist
from lib.actor import Point

class Checkpoint:
    def __init__(self, x: float, y: float, radius: float = 36.0, name: str = ""):
        self.x = x
        self.y = y
        self.radius = radius
        self.name = name

    def pos(self) -> Point:
        return (self.x, self.y)

    def contains(self, pt: Point) -> bool:
        return dist((self.x, self.y), pt) <= self.radius


# 13 checkpoint sequenziali attorno alla pista super-sprint-1
CIRCUIT_1_CHECKPOINTS = [
    Checkpoint(240, 72, 36, "Traguardo / Partenza"),
    Checkpoint(380, 72, 36, "Rettilineo Superiore"),
    Checkpoint(435, 115, 36, "Curva 1 Nord-Est"),
    Checkpoint(445, 200, 36, "Discesa Est"),
    Checkpoint(435, 290, 36, "Ingresso Curva Sud-Est"),
    Checkpoint(405, 330, 36, "Curva Sud-Est"),
    Checkpoint(340, 305, 36, "Chicane Est"),
    Checkpoint(250, 260, 36, "Chicane Centro"),
    Checkpoint(170, 285, 36, "Chicane Ovest"),
    Checkpoint(90, 315, 36, "Curva Sud-Ovest"),
    Checkpoint(72, 220, 36, "Risalita Ovest"),
    Checkpoint(72, 120, 36, "Curva Nord-Ovest"),
    Checkpoint(140, 72, 36, "Rettilineo Finale")
]


class CheckpointManager:
    def __init__(self, checkpoints: list[Checkpoint] = None, target_laps: int = 3):
        self._checkpoints = checkpoints if checkpoints is not None else list(CIRCUIT_1_CHECKPOINTS)
        self._target_laps = target_laps

    @property
    def target_laps(self) -> int:
        return self._target_laps

    @property
    def count(self) -> int:
        return len(self._checkpoints)

    def get_checkpoint(self, index: int) -> Checkpoint:
        return self._checkpoints[index % len(self._checkpoints)]

    def get_all(self) -> list[Checkpoint]:
        return list(self._checkpoints)

    def update_car(self, car) -> bool:
        target_idx = car.target_checkpoint_index
        target_cp = self._checkpoints[target_idx]
        car_center = car.center

        if target_cp.contains(car_center):
            car.advance_checkpoint(len(self._checkpoints))
            return True
        return False

    def rank_cars(self, cars: list) -> list:
        def rank_key(car):
            target_cp = self.get_checkpoint(car.target_checkpoint_index)
            d = dist(car.center, target_cp.pos)
            # Punteggio sintetico continuo: giri * 10000 + passaggi * 100 - distanza
            return (car.laps, car.total_checkpoints_hit, -d)

        return sorted(cars, key=rank_key, reverse=True)
