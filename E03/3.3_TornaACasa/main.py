from random import randrange as rn
import g2d as g

ARENA_DIM = (240, 240)
ARENA_H, ARENA_W = ARENA_DIM
ARENA_CENTRE = (ARENA_H / 2, ARENA_W / 2)
DIRECTIONS = [(0, -4), (-4, 0), (0, 4), (4, 0)]
BALL_RADIUS = 4

class Ball:
    def __init__(self, homex, homey):
        self._dx, self._dy = DIRECTIONS[rn(len(DIRECTIONS))]
        self._home = (homex, homey)
        self._x , self._y = self._home

    def pos(self):
        return (self._x, self._y)

    def randDir(self):
        self._dx, self._dy = DIRECTIONS[rn(len(DIRECTIONS))]

    def goHome(self):
        self._x, self._y = self._home

    def checkPos(self):
        if (self._x + self._dx) >= ARENA_W or (self._x + self._dx) <= 0 or (self._y + self._dy) >= ARENA_H or (self._y + self._dy) <= 0:
            self.randDir()
            self.goHome()

    def reDraw(self):
        g.draw_circle(self.pos(), BALL_RADIUS)

    def move(self):
        self.checkPos()
        self._x += self._dx
        self._y += self._dy
        self.reDraw()

def main():
    palla1 = Ball(rn(0, ARENA_H), rn(0, ARENA_W))
    palla2 = Ball(rn(0, ARENA_H), rn(0, ARENA_W))

    g.init_canvas(ARENA_DIM)

    def tick():
        g.clear_canvas()
        palla1.move()
        palla2.move()

    g.main_loop(tick)

if __name__ == "__main__":
    main()