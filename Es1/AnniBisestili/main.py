anno = int(input("inserire un anno: "))

if ((anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0)) : print("l'anno è bisestile")
else : print("l'anno non è bisestile")
