'''
Definire una funzione draw_figure

    Parametri per: centro, raggio, n
    Disegnare una figura di n cerchi concentrici
    Il raggio più interno è 1/n rispetto al più esterno
    Colorare i cerchi in grigio: dal nero esterno al bianco interno

In main:

    Chiedere all'utente un numero n
    In un canvas 500×500, disegnare n figure uguali affiancate
    Occupare tutto lo spazio, in orizzontale

'''

import g2d as g

CANVASW, CANVASL = 500, 500
CANVASSIZE = (CANVASW, CANVASL)

def drawFigure(center: (int, int), maxRadius: float, n: int) -> None:
    for i in range(n):
        radius = (maxRadius / n) * (n - i)
        colVal = int(i * (255 / (n - 1)))
        color = (colVal, colVal, colVal)
        g.set_color(color)
        g.draw_circle(center, radius)

def main():
    n = int(input("How many circles?: "))
    g.init_canvas(CANVASSIZE)

    diameter = CANVASW / n
    radius = diameter / 2
    y = CANVASL / 2

    for j in range(n):
        x = radius + j * diameter
        drawFigure((x, y), radius, n)
    
    g.main_loop()

if __name__ == "__main__":
    main()