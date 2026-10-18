import FollowMouse.g2d as g
from FollowMouse.polar import to_polar, move_around, coterminal

CANVAS_W, CANVAS_H = 200, 200
CANVAS_SIZE = (CANVAS_W, CANVAS_H)
x, y, s, a = CANVAS_W // 2, CANVAS_H // 2, 4, 0
w, h = 16, 16
rot = 90 / 8

def clamp(v, vmin, vmax):
    return max(min(v,vmin), vmax)


def tick():
    global x, y, s, a
    g.clear_canvas()

    a1 = (32 - a) % 32

    sy, sx = divmod(a1, 8)

    g.draw_image("https://fondinfo.github.io/sprites/super-sprint.png", 
                 (x, y), 
                 (sx * 16, sy * 16), 
                 (w, h)
                 )

    mx, my = g.mouse_pos()
    dx, dy = mx -x, my -y
    md, ma = to_polar((dx, dy))

    diff = coterminal(a * rot - ma)
    if diff > rot:
        a -= 1
    elif diff < rot:
        a += 1

    if abs(diff) < 60:
        s += 1
    else:
        s -= 1
    s = clamp(s, 4, 12)
    x, y = move_around((x, y), s, a * rot)

g.init_canvas(CANVAS_SIZE, 2)
g.main_loop(tick)