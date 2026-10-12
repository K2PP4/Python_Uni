from random import randint as rnd
import g2d as g

ARENA_H, ARENA_W = 240, 240
BALLSIZE = 5

class Ball:
    def __init__(self):
        self._x = ARENA_H / 2
        self._y = ARENA_W / 2
        self._dx = rnd(-5, 5)
        self._dy = rnd(-5, 5)

    def __str__(self):
        return f"Ball position: ({self._x}, {self._y})"

    def getPos(self):
        return (self._x, self._y)

    def rndDir(self):
        if((self._x + self._dx) >= ARENA_W):
            self._dx = rnd(-5, -1)
        if((self._x + self._dx) <= 0):
            self._dx = rnd(1, 5)
        if((self._y + self._dy) >= ARENA_H):
            self._dy = rnd(-5, -1)
        if((self._y + self._dy) <= 0):
            self._dy = rnd(1, 5)

    def redraw(self):
        g.clear_canvas()
        g.draw_circle(self.getPos(), BALLSIZE)

    def move(self):
        self.rndDir()
        self._x += self._dx
        self._y += self._dy
        self.redraw()
        print(self)


def main():
    palla = Ball()

    g.init_canvas((ARENA_H, ARENA_W))
    g.main_loop(palla.move, 60)

if __name__ == "__main__":
    main()