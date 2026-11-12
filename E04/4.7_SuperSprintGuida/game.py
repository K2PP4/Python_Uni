"""
Rendere la classe Car un actor
• Aggiungerla all'arena fornita, 500x500, con spawn
• Sterzata
    • Se l'utente preme la freccia verso destra, o
    sinistra
    • Cambiare direzione gradualmente, variazione fissa
    a ogni frame
• Accelerazione e frenata
    • Se l'utente preme la freccia verso alto, o basso
    • Cambiare velocità gradualmente, variazione fissa a ogni frame
• Prendere i tasti da arena.current_keys()
"""

import g2d as g
import polar as p

from actor import Actor, Arena

BACKGROUND_URL = "super-sprint-bg.png"
ARENA_H, ARENA_W = 500, 500
ARENA_SIZE = (ARENA_W, ARENA_H)

class Car(Actor):
    def __init__(self, pos: tuple[int, int], color: int = 0):
        self._pos = pos
        self._color = color
        self._size = (16,16)
        self._speed = 4
        self._angle = 0.0
        self._angle_inc = 90 / 8
        self._max_speed = 5
        self._min_speed = 1
        self._sprite_url = "super-sprint.png"
    
    def pos(self) -> tuple[int, int]:
        return self._pos

    def size(self) -> tuple[int, int]:
        return self._size

    def sprite(self) -> tuple[str, tuple[int, int], tuple[int, int]]:
        sprite_angle = 360 - (self._angle % 360)
        dir_index = (int(sprite_angle * 4) // 45) % 32

        dir_col = dir_index % 8
        dir_row = dir_index // 8

        color_x_block = self._color % 2
        color_y_block = self._color // 2

        clip_x = (color_x_block * 8 + dir_col) * 16
        clip_y = (color_y_block * 4 + dir_row) * 16

        return self._sprite_url, (clip_x, clip_y), self._size

    def _change_speed(self, arena: Arena):
        active_keys = arena.current_keys()

        print(active_keys)

        if "up" in active_keys and "down" not in active_keys:
            self._speed = min(self._speed + 1, self._max_speed)
        elif "down" in active_keys and "up" not in active_keys:
            self._speed = max(self._speed - 1, self._min_speed)

    def _change_direction(self, arena: Arena):
        active_keys = arena.current_keys()

        if "left" in active_keys and "right" not in active_keys:
            self._angle += self._angle_inc
        if "right" in active_keys and "left" not in active_keys:
            self._angle -= self._angle_inc

    def move(self, arena: Arena):
        self._change_speed(arena)
        self._change_direction(arena)

        self._pos = p.move_around(self._pos, self._speed, self._angle)


yellow_car = Car((250, 250))
arena = Arena(ARENA_SIZE)

def tick():
    g.clear_canvas()
    arena.tick(g.current_keys())

    img_src, clip_pos, clip_size = yellow_car.sprite()
    g.draw_image(img_src, yellow_car.pos(), clip_pos, clip_size)


def main():
    g.init_canvas(ARENA_SIZE)
    arena.spawn(yellow_car)
    g.main_loop(tick)

if __name__ == "__main__" : main()
