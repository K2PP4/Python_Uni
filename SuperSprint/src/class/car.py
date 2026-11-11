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
