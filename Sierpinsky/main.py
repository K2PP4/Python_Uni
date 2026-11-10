import g2d

CANVAS_W, CANVAS_H = 800, 800
MIN_SIZE = 5

def sierp(x, y, w, h):
    size = (w/2, h/2)
    if min(size) < MIN_SIZE:
        return

    g2d.set_color((255,255,255))
    g2d.draw_rect((x, y), size)
    
    sierp(x + w//2, y, w-w//2, h/2)
    sierp(x, y + h//2, w//2, h-h//2)
    sierp(x + w//2, y + h//2, w-w//2, h-h//2)

g2d.init_canvas((CANVAS_W, CANVAS_H))
g2d.set_color((0,0,0))
g2d.clear_canvas((0,0,0))
sierp(0, 0, CANVAS_W, CANVAS_H)
g2d.main_loop()