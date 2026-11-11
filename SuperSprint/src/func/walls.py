from math import dist
from lib.actor import Actor, Arena, Point

def actor_center(a: Actor) -> Point:
    x, y, w, h = a.pos() + a.size()
    return (x + w / 2, y + h / 2)

class CurvedWall(Actor):
    def __init__(self, pos: Point, size: Point, center: Point, radius: float):
        self._pos = pos
        self._size = size
        self._center = center
        self._radius = radius

    def move(self, arena: Arena):
        pass

    def pos(self) -> Point:
        return self._pos

    def size(self) -> Point:
        return self._size

    def sprite(self) -> Point | None:
        return None

    def center(self) -> Point:
        return self._center

    def radius(self) -> float:
        return self._radius

class ExternalWall(CurvedWall):  # attract cars towards center
    def confirm_collision(self, other: Actor) -> bool:
        return dist(self.center(), actor_center(other)) > self.radius()

class InternalWall(CurvedWall):  # repel cars from center
    def confirm_collision(self, other: Actor) -> bool:
        return dist(self.center(), actor_center(other)) < self.radius()

def load_walls(filename: str) -> list[str]:
    walls = []
    with open(filename) as file:
        for line in file:
            walls.append(line.strip())
    return walls

def is_wall(x, y, walls) -> bool:
    return walls[int(y)][int(x)] == "#"