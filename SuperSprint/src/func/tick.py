from lib import g2d
from lib.polar import move_around, to_polar, coterminal

CANVAS_W, CANVAS_H = 200, 200
x, y = CANVAS_W // 2, CANVAS_H // 2
speed, angle = 4, 0
w, h = 16, 16
rot = 90 / 8

def clamp(v, vmin, vmax):
    return min(max(v, vmin), vmax)

def tick():
    global x, y, speed, angle
    g2d.clear_canvas()
    
    sprite_y, sprite_x = divmod(-angle % 32, 8)
    g2d.draw_image("/img/super-sprint.png",
                   (x, y), (sprite_x * w, sprite_y * h), (w, h))
    
    mouse_x, mouse_y = g2d.mouse_pos()
    vec = mouse_x - x, mouse_y - y
    mouse_dist, mouse_angle = to_polar(vec)
    
    diff = coterminal(angle * rot - mouse_angle)
    if diff > rot:
        angle -= 1
    elif diff < -rot:
        angle += 1

    if abs(diff) < 60:
        speed += 1
    else:
        speed -= 1
    speed = clamp(speed, 2, 8)
        
    x, y = move_around((x, y), speed, angle * rot)