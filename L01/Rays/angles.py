from math import pi, sin, cos, radians
import g2d as g

def drawRays(x0: int, y0:int, r: int):
    for angle in [0, 15, 30, 45]:
        x = x0 + r * cos(radians(angle))
        y = y0 + r * sin(radians(angle))
        g.draw_line((x0, y0), (x,y))

g.init_canvas((500,500))
drawRays(200,200,100)
g.main_loop()