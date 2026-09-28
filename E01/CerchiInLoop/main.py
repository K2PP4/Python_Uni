import g2d as g
from random import randint as r


raggi = []
center = (250, 250)

for _ in range(3):
    x = float(input("inserisci il raggio del cerchio"))
    raggi.append(x)

g.init_canvas((500,500))

for x in raggi :
    g.set_color((r(0, 255), r(0,255), r(0,255)))
    g.draw_circle(center, x)

g.main_loop()
