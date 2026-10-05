import lib.g2d as g
from lib.polar import move_around

x, y, speed, steeringAngle = 80, 80, 4, -30
ARENA_W, ARENA_H = 480, 360

def tick():
    global x, y, speed, steeringAngle
    g.clear_canvas()
    g.draw_image("ball.png", (x,y))

    if g.mouse_clicked():
        mx, my = g.mouse_pos()

    x, y = move_around((x, y), speed, steeringAngle)