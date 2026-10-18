'''
Creare una classe Car, partendo dall'esempio Ball

    Modulo della velocità sempre pari a 4

Campo angle per memorizzare la direzione
Metodo move, per aggiornare la posizione

    Ogni 2 frame, incrementare angle di una quantità fissa
    Inizialmente l'incremento angolare è di 90/8
    Ogni 64 frame, passare da rotazione oraria a antioraria e viceversa (cambiare il segno dell'incremento angolare)

Metodo sprite

    Ritagliare l'immagine da super-sprint.png
    Scegliere l'immagine in base al valore attuale del campo angle

'''

import g2d as g
import polar as p

ANGLE_INC = 90/8
SPRITE_URL = "super-sprint.png"
MAP_URL = "super-sprint-bg.png"
MAP_SIZE = (256, 210)

class Car:
    def __init__(self, pos: tuple[int, int], color: int = 0):
        self._pos = pos
        self._color = color
        self._size = (16,16)
        self._speed = 4
        self._angle = 0.0
        self._angle_inc = ANGLE_INC
        self._frame = 0

    def move(self):
        self._frame += 1

        if self._frame % 64 == 0:
            self._angle_inc *= -1
        
        if self._frame % 2 == 0:
            self._angle = (self._angle + self._angle_inc) % 360

        self._pos = p.move_around(self._pos, self._speed, self._angle)
    
    def pos(self) -> tuple[int, int]:
        return self._pos

    def sprite(self) -> tuple[str, tuple[int, int], tuple[int, int]]:
        spriteAngle = 360 - (self._angle % 360)
        dirIndex = (int(spriteAngle * 4) // 45) % 32

        dirCol = dirIndex % 8
        dirRow = dirIndex // 8

        colorXBlock = self._color % 2
        colorYBlock = self._color // 2

        clipX = (colorXBlock * 8 + dirCol) * 16
        clipY = (colorYBlock * 4 + dirRow) * 16

        return SPRITE_URL, (clipX, clipY), self._size

car = Car(pos=(MAP_SIZE[0] / 2, MAP_SIZE[1] / 2), color=0) # Gialla = 0, Blu = 1, Rossa = 2, Bianca = 3

def tick():
    car.move()
    g.clear_canvas()

    imgSrc, clipPos, clipSize = car.sprite()
    g.draw_image(imgSrc, car.pos(), clipPos, clipSize)

def main():
    g.init_canvas(MAP_SIZE, scale=2)
    g.main_loop(tick)

if __name__ == "__main__":
    main()