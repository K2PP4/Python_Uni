"""
• Definire una funzione regular_poly
    • Parametri: numero n dei lati, centro p e raggio r del cerchio circoscritto, angolo a del primo vertice
    • Trovare gli n vertici attorno al centro con move_around, tutti a distanza r
    • Restituire una lista con tutti i punti del poligono, ciascuno rappresentato come una tupla
• Funzioni main e tick
    • Chiamare regular_poly con dati dell'utente
    • Unire i vertici (anche l'ultimo al primo) per disegnare un poligono al centro del canvas
    • Mostrare rotazione del poligono attorno al centro
"""

import g2d as g
import polar as p
from g2d import Point

nSides = 0
center = (0,0)
radius = 0.0
angle = 0.0

def regular_poly(nSides: int, center: Point, radius: float, angle: float) -> list[Point]:
    points = []
    stepAngle = 360 / nSides
    
    for i in range(nSides):
        vertexAngle = angle + i * stepAngle
        vertex = p.move_around(center, radius, vertexAngle)
        points.append(vertex)

    return points

def tick():
    global angle
    g.clear_canvas()

    angle = (angle + 1) % 360

    points = regular_poly(nSides, center, radius, angle)

    for i in range(len(points)):
        pt1 = points[i]
        pt2 = points[(i + 1) % len(points)]
        g.draw_line(pt1, pt2)

def main():
    global nSides, center, radius, angle
    
    nSides = int(input("insert the number of sides [integer]: "))
    x_str, y_str = input("insert (x,y) of the center [integer, integer]: ").split(',')
    center = (float(x_str), float(y_str))
    radius = float(input("insert the radius of the inscrypted circle [float]: "))
    angle = float(input("insert the angle value in degrees [float]: "))
    
    g.init_canvas((600, 600))
    g.main_loop(tick)

if __name__ == "__main__":
    main()
