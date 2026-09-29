import g2d as g

x, y, dx = 80, 80, 4
ARENA_W, ARENA_H = 480, 360

def tick():
    global x, dx
    g.clear_canvas()
    g.draw_rect((x,y), (20,20))

    x = x + dx

g.init_canvas((ARENA_W, ARENA_H))
g.main_loop(tick)