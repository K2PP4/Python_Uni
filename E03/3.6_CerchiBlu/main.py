'''
3.6 - Cerchi blu

 * chiedere all'utente un numero 'n'
 * disegnare una riga di 'n' cerchi blu 
   - affiancati, su canvas 500x500
   - intensità di blu linearmente crescente
 * disegno simile alla figura però...
   - lasciare un margine di 25px dai bordi
   - intensità di blu del primo cerchio 50
   - intensità dell'ultimo 200
'''

import g2d as g

CANVASW, CANVASL = 500, 500
CANVASSIZE = (CANVASW, CANVASL)
SIZE = 50
PADDING = 25

def main():
  n_cerchi = int(input("Quanti cerchi? "))
  g.init_canvas(CANVASSIZE)
  
  usable_w = CANVASW - (2 * PADDING)
  diameter = usable_w / n_cerchi
  radius = diameter / 2
  y = PADDING + radius

  for n in range(n_cerchi):
    x = PADDING + radius + (n * diameter)

    blu = int(50 + n * (150 / (n_cerchi -1)))

    g.set_color((0, 0, blu))
    g.draw_circle((x, y), radius)
  
  g.main_loop()

if __name__ == "__main__":
  main()
