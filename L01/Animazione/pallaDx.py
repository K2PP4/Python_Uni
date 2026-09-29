import g2d as g

x, y, dx = 80, 80, 4
ARENA_W, ARENA_H = 480, 360
BALLSIZE = 16

def tick():
    global x, dx
    g.clear_canvas()
    g.draw_image("ball.png", (x,y))

    if g.mouse_clicked():
        dx = -dx

    if (x + dx) + BALLSIZE > ARENA_W or (x + dx) < 0 : 
        dx = -dx

    
    x = x + dx

g.init_canvas((ARENA_W, ARENA_H))
g.main_loop(tick)