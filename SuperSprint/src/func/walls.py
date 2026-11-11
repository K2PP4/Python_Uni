from actor import Actor, Arena
from math import dist

def actor_center(a: Actor) -> Point:
    x, y, w, h = a.pos() + a.size()
    return (x + w / 2, y + h / 2)

class CurvedWall(Actor):
    def __init__(self, pos, size, center, radius):
        self._pos = pos
        self._size = size
        self._center = center
        self._radius = radius
    
    def move(self, arena):
        pass
    
    def pos(self):
        return self._pos
    
    def size(self):
        return self._size
    
    def sprite(self):
        return None
    
    def center(self):
        return self._center
    
    def radius(self):
        return self._radius

class ExternalWall(CurvedWall):  # attract cars towards center
    def confirm_collision(self, other: Actor) -> bool:
        return dist(self.center(), actor_center(other)) > self.radius()

class InternalWall(CurvedWall):  # repel cars from center
    def confirm_collision(self, other: Actor) -> bool:
        return dist(self.center(), actor_center(other)) < self.radius()

class Car(Actor):  # …
    def move(self, arena):
        for other in arena.collisions():
            if isinstance(other, ExternalWall) and other.confirm_collision(self):
                # …
                pass

def load_walls(filename) -> list[str]:
    walls = []
    with open(filename) as file:
        for line in file:
            walls.append(line.strip())
    return walls

def is_wall(x, y, walls) -> bool:
    return walls[int(y)][int(x)] == "#"