from random import randint as rnd
import g2d as g

ARENA_W = 250
ARENA_L = 250
ARENA_SIZE = (ARENA_W, ARENA_L)
RADIUS = 16

def printCircles(nCircles, centerX, centerY):

    startX = centerX - (nCircles - 1) * RADIUS

    for n in range(nCircles):
        g.set_color((rnd(0, 255), rnd(0, 255), rnd(0, 255)))
        g.draw_circle((startX + n * RADIUS * 2, centerY), RADIUS)

def main():
    nRows = int(input("insert a number of rows: "))
    
    g.init_canvas(ARENA_SIZE, 1.5)
    for n in range(nRows):
        printCircles(n + 1, ARENA_W / 2, (n + 1) * RADIUS * 2)
    
    g.set_color((rnd(0, 255), rnd(0, 255), rnd(0, 255)))
    g.draw_circle((ARENA_W / 2, (nRows + 1) * RADIUS * 2), RADIUS)
    g.main_loop()

if __name__ == "__main__":
    main()
