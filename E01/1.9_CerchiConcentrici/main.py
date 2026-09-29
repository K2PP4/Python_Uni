import g2d as g
from random import randint as rnd

ARENA_W, ARENA_H = 500, 500
CENTER = (ARENA_H/2, ARENA_H/2)

g.init_canvas((ARENA_W, ARENA_H))

maxrad = 200
radius = rnd(0,maxrad-1)

g.set_color((rnd(0,255),rnd(0,255),rnd(0,255)))
g.draw_circle(CENTER, maxrad)

while radius >= 10 :
    g.set_color((rnd(0,255),rnd(0,255),rnd(0,255)))
    g.draw_circle(CENTER, radius)

    maxrad -= radius
    radius = rnd(0, maxrad)

    print(radius)

g.main_loop()