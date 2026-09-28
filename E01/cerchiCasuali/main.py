# inserire n cerchi da disegnare
# punti casuali
# raggio 50

import g2d as g
from random import randint as rnd

nCerchi = int(input("Inserire il numero di cerchi da disegnare: "))

g.init_canvas((500,500))

for _ in range(nCerchi):
    g.set_color((rnd(0,255),rnd(0,255),rnd(0,255)))
    g.draw_circle((rnd(50,450),rnd(50,450)), 50)

g.main_loop()