from random import randint as rnd
import g2d as g

SIZE_CIRCLE = 16
ARENA_W = 250
ARENA_L = 250
ARENA_SIZE = (ARENA_W, ARENA_L)

def printCircles(nCircles, centerX, centerY):
    for n in range(0, nCircles):
        g.set_color((rnd(0, 255), rnd(0, 255), rnd(0, 255)))
        g.draw_circle((centerX * (n + 1) * 2, centerY), SIZE_CIRCLE)

def main():
    nRows = int(input("insert a number of rows: "))
    
    g.init_canvas(ARENA_SIZE, 1.5)
    for n in range(0, nRows):
        printCircles(n + 1, SIZE_CIRCLE, (n + 1) * SIZE_CIRCLE * 2)
    g.main_loop()

if __name__ == "__main__":
    main()
