import g2d as g
from polar import move_around, to_polar, dist

ARENA_W, ARENA_H = 400, 400
BALLSIZE = 20

v = 4
a = 0
x, y = 200, 200

def tick():
    global x, y, a, v
    g.clear_canvas()

    (x, y) = move_around((x, y), v, a)

    if g.mouse_clicked() :
        (mx, my) = g.mouse_pos()
        if mx > x :
            a += 90/8
        elif mx < x :
            a -= 90/8

    g.draw_image("ball.png", (x,y))

g.init_canvas((ARENA_W, ARENA_H))
g.main_loop(tick)