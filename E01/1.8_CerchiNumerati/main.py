import g2d as g
from random import randint as rnd

nCircles = int(input("Inserire il numero di cerchi da disegnare: "))

g.init_canvas((500, 500))

for n in range(nCircles):
    # --- Position Variables ---
    x = rnd(50, 445)
    y = rnd(50, 445)
    # --- Offset Variables ---
    x_offset = 5
    y_offset = 5
    # --- RGB Variables
    red = rnd(0, 255)
    green = rnd(0, 255)
    blue = rnd(0, 255)
    
    if red + green + blue > 382 : isLight = True
    else : isLight = False

    g.set_color((66,66,66))
    g.draw_circle((x + x_offset, y + y_offset), 50)
    g.set_color((red, green, blue))
    g.draw_circle((x, y), 50)
    if isLight : 
        g.set_color((0,0,0))
        g.draw_text(str(n), (x,y), 24)
    else :
        g.set_color((255,255,255))
        g.draw_text(str(n), (x,y), 24)

g.main_loop()