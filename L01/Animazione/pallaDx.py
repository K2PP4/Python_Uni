import g2d as g

x, y, dx, dy = 80, 80, 4, 4
ARENA_W, ARENA_H = 480, 360
BALLSIZE = 20

def tick():
    global x, dx, y, dy
    g.clear_canvas()
    g.draw_image("ball.png", (x,y))

    if g.mouse_clicked():
        dx = -dx

    if (x + dx) + BALLSIZE > ARENA_W or (x + dx) < 0 : 
        dx = -dx

    if (y + dy) + BALLSIZE > ARENA_H or (y + dy) < 0 :
        dy = -dy

    
    x += dx
    y += dy

g.init_canvas((ARENA_W, ARENA_H))
g.main_loop(tick)