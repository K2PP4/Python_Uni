ARENA_H, ARENA_W = 400, 400

class Ball:
    def __init__(self, x0, y0):
        self._x = x0
        self._y = y0
        self._dx = 5
        self._dy = 5
        self._size = 16

    def move(self):
        if self._x + self._dx < 0 or self._x + self._dx > ARENA_W - self._size:
            self._dx = -self._dx
        if self._y + self._dy < 0 or self._y + self._dy > ARENA_H - self._size:
            self._dy = -self._dy
            
        self._x += self._dx
        self._y += self._dy

    def pos(self):
        return (
            self._x,
            self._y
        )