import g2d as g
from math import sqrt

def calDistance(x0, y0, x, y, n) -> tuple:

    distancel = (x - x0) / (n - 1)
    distanceh = (y - y0) / (n - 1)

    return (distancel, distanceh)

def main():
    CANVAS_H, CANVAS_L = 400, 400
    POINT_RADIUS = 5

    nPoints = int(input("insert the number of points to be drawn: "))
    firstPointX = int(input("insert the X value of the first point: "))
    firstPointY = int(input("insert the Y value of the first point: "))
    lastPointX = int(input("insert the X value of the last point: "))
    lastPointY = int(input("insert the Y value of the last point: "))

    distances = calDistance(firstPointX, firstPointY, lastPointX, lastPointY, nPoints)

    g.init_canvas((CANVAS_H, CANVAS_L))
    
    for i in range(0, nPoints):
        g.draw_circle((firstPointX + i * distances[0], firstPointY + i * distances[1]), POINT_RADIUS)

    g.main_loop()

main()