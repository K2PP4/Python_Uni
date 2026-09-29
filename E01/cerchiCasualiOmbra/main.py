# inserire n cerchi da disegnare
# punti casuali
# raggio 50

import g2d as g
from random import randint as rnd

nCerchi = int(input("Inserire il numero di cerchi da disegnare: "))

g.init_canvas((500, 500))

for _ in range(nCerchi):
    x = rnd(50, 445)
    y = rnd(50, 445)
    x_offset = 5
    y_offset = 5

    g.set_color((66,66,66))
    g.draw_circle((x + x_offset, y + y_offset), 50)
    g.set_color((rnd(0,255),rnd(0,255),rnd(0,255)))
    g.draw_circle((x, y), 50)

g.main_loop()