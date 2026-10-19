"""
Modificare Ball nell'esempio bounce (con Arena)
• https://fondinfo.github.io/play/?c07_bounce.py
• Mantenere gli stessi campi: x, y, w, h, dx, dy
• A ogni rimbalzo, il raggio aumenta di 2 pixel
• Fino a un massimo di 20 pixel, poi torna a 10
• Definire metodo grow, senza parametri oltre self
• Calcolare la posizione centrale e il raggio attuali
• Modificare il raggio come richiesto (var locale)
• Rivalutare x, y, w, h della pallina
• Restituire None nel metodo sprite
• Nel tick, disegnare un rettangolo quando lo sprite è None
"""

from random import choice, randrange
from actor import Actor, Arena, Point
import g2d as g

ARENAW, ARENAL = 250, 500
ARENASIZE = (ARENAW, ARENAL)

arena = Arena(ARENASIZE)

class Ball(Actor):
    def __init__(self, pos):
        self._x, self._y = pos
        self._w, self._h = 20, 20
        self._dx, self._dy = 4, 4

    def grow(self):
        _radius = self._w // 2
        centerX = self._x + _radius
        centerY = self._y + _radius

        _radius += 2
        if _radius > 20: _radius = 10

        self._w = _radius * 2
        self._h = self._w
        self._x = centerX - _radius
        self._y = centerY - _radius

    def move(self, arena: Arena):
        bounced = False

        for other in arena.collisions():
            if not isinstance(other, Ghost):
                x, y = other.pos()
                if x < self._x:
                    self._dx = abs(self._dx)
                else:
                    self._dx = -abs(self._dx)
                if y < self._y:
                    self._dy = abs(self._dy)
                else:
                    self._dy = -abs(self._dy)
                bounced = True

        arena_w, arena_h = arena.size()
        if self._x + self._dx < 0:
            self._dx = abs(self._dx)
            bounced = True
        elif self._x + self._dx > arena_w - self._w:
            self._dx = -abs(self._dx)
            bounced = True
        if self._y + self._dy < 0:
            self._dy = abs(self._dy)
            bounced = True
        elif self._y + self._dy > arena_h - self._h:
            self._dy = -abs(self._dy)
            bounced = True

        if bounced: self.grow()

        self._x += self._dx
        self._y += self._dy

    def pos(self) -> Point:
        return self._x, self._y

    def size(self) -> Point:
        return self._w, self._h

    def sprite(self) -> Point:
        return None

def tick():
    global arena
    arena.tick()

    g.clear_canvas()

    for a in arena.actors():
        if a.sprite() is None:
            g.draw_rect(a.pos(), a.size())
        else:
            g.draw_image("sprites.png", a.pos(), a.sprite())

def main():
    g.init_canvas(ARENASIZE)
    ball = Ball((0,0))
    arena.spawn(ball)
    g.main_loop(tick)

if __name__ == "__main__" : main()