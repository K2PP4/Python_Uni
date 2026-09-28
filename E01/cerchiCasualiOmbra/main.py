# inserire n cerchi da disegnare
# punti casuali
# raggio 50

import g2d as g
from random import randint as rnd

nCerchi = int(input("Inserire il numero di cerchi da disegnare: "))

g.init_canvas((500, 500))

for _ in range(nCerchi):
    x = rnd(50, 450)
    y = rnd(50, 450)
    x_offset = 5
    y_offset = 5

    # gestione ombre
    # sx up x = x, y = y, xs = x+5, ys = y+5
    # dx up x -= 5, y = y, xs = x+5, ys = y+5
    # sx dn x = x, y -= 5, xs = x+5, ys = y+5
    # dx dn x -= 5, y -= 5, xs = x+5, ys = y+5

g.main_loop()