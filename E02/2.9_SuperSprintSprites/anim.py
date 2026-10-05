import g2d as g
from polar import move_around

ARENA_W, ARENA_H = 256, 224
CARSIZE = 16

v = 1
a = 0
x, y = ARENA_W / 2, ARENA_H / 2

def check_bounds():
    global x, y, a
    if x < 0:
        x = 0
    elif x > ARENA_W - CARSIZE:
        x = ARENA_W - CARSIZE
    if y < 0:
        y = 0
    elif y > ARENA_H - CARSIZE:
        y = ARENA_H - CARSIZE

def checkMouse():
    global a
    if g.mouse_clicked():
        (mx, my) = g.mouse_pos()
        if mx > ARENA_W / 2:
            a += 90 / 8
        elif mx < ARENA_W / 2:
            a -= 90 / 8

def drawBg(level: int):
    if level > 4:
        g.draw_image("super-sprint-bg.png", (0, 0), (ARENA_W * (level - 4), ARENA_H), (ARENA_W, ARENA_H))
    else:
        g.draw_image("super-sprint-bg.png", (0, 0), (ARENA_W * level, 0), (ARENA_W, ARENA_H))

def carUpdate(x, y, a ):
    clip_pos = (0, 0)
    clip_size = (CARSIZE, CARSIZE)

    spriteAngle = 360 -(a % 360)                                    # Remap angle to (0 - 360) and invert it to match the sprite sheet orientation
    spriteIndex = (int(spriteAngle * 4) // 45) % 32                 # Mapping angle to sprite index (0 - 31)
    row = spriteIndex // 8                                          # Determine the row of the sprite
    col = spriteIndex % 8                                           # Determine the column of the sprite

    clip_pos = (col * CARSIZE, row * CARSIZE)                       # Calculate the position of the sprite in the sprite sheet
    # Note: To change the sprite color just add and offset to the clip_pos, for example: clip_pos = (col * CARSIZE + 128, row * CARSIZE) will use the blue car sprite.

    g.draw_image("super-sprint.png", (x,y), clip_pos, clip_size)

def tick():
    global x, y, a, v
    g.clear_canvas()

    drawBg(0)

    (x, y) = move_around((x, y), v, a)

    check_bounds()

    checkMouse()

    carUpdate(x, y, a)

def main():
    g.init_canvas((ARENA_W, ARENA_H))
    g.main_loop(tick)

main()