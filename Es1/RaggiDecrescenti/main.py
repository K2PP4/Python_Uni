import Lib.g2d as g

dimCanvas = (500, 500)
centre = (250, 250)

okRaggi = False

while not okRaggi:
    r1 = int(input("Inserisci il raggio del primo cerchio: "))
    r2 = int(input("Inserisci il raggio del secondo cerchio: "))
    r3 = int(input("Inserisci il raggio del terzo cerchio: "))

    if r1 > r2 and r2 > r3:
        okRaggi = True
        g.init_canvas(dimCanvas)
        g.set_color((255, 0, 255)) #magenta
        g.draw_circle(centre, r1)
        g.set_color((0, 255, 255)) #ciano
        g.draw_circle(centre, r2)
        g.set_color((255, 255, 0)) #giallo
        g.draw_circle(centre, r3)
        g.main_loop()
    else :
        print("I raggi non sono in ordine decrescente. Riprova.")
