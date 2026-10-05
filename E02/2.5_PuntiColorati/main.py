import g2d as g
from math import sqrt

def calDistance(x0, y0, x, y, n) -> tuple:

    distancel = (x - x0) / (n - 1)
    distanceh = (y - y0) / (n - 1)

    return (distancel, distanceh)

def main():
    CANV_H, CANV_L = 400, 400
    POINT_RADIUS = 5

    nPoints = int(input("insert the number of points to be drawn: "))
    firstPointX = int(input("insert the X value of the first point: "))
    firstPointY = int(input("insert the Y value of the first point: "))
    lastPointX = int(input("insert the X value of the last point: "))
    lastPointY = int(input("insert the Y value of the last point: "))
    
    f_color = tuple(map(int, input("what should the color of the first point be? [r,g,b]: ").split(',')))
    l_color = tuple(map(int, input("what should the color of the last point be? [r,g,b]: ").split(',')))

    distances = calDistance(firstPointX, firstPointY, lastPointX, lastPointY, nPoints)

    r_diff = (l_color[0] - f_color[0]) / (nPoints - 1)
    g_diff = (l_color[1] - f_color[1]) / (nPoints - 1)
    b_diff = (l_color[2] - f_color[2]) / (nPoints - 1)

    g.init_canvas((CANV_H, CANV_L))

    for i in range(0, nPoints):
        current_r = int(f_color[0] + r_diff * i)
        current_g = int(f_color[1] + g_diff * i)
        current_b = int(f_color[2] + b_diff * i)
        
        g.set_color((current_r, current_g, current_b))
        g.draw_circle((firstPointX + i * distances[0], firstPointY + i * distances[1]), POINT_RADIUS)

    g.main_loop()


main()