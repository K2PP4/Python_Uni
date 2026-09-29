anniUtente = int(input("Quanti anni hai? "))

if (anniUtente > 0 and anniUtente <= 25):
    print("Hai diritto allo sconto studenti!!")
elif (anniUtente < 0) :
    print("Età non valida.")
else :
    print("Prezzo intero")
    
