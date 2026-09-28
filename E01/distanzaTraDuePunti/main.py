from math import sqrt

x1 = float(input("prima x: "))
y1 = float(input("prima y: "))
x2 = float(input("seconda x: "))
y2 = float(input("seconda y: "))

if (x1 == x2): print("i punti sono allineati verticalmente")
if (y1 == y2): print("i punti sono allineati orizzontalmente")

d = sqrt(((x2-x1)**2)+((y2-y1)**2))
print("la distanza d tra i due punti vale " + str(d))
