# Definire una funzione ricorsiva recursive_pow per calcolare la potenza intera positiva di un numero
# • Per qualsiasi numero x, x° = 1
# • La potenza n-esima di un numero x si può calcolare come:
# • Prodotto tra x e la potenza n - 1 di x (ricorsione)
# • In una funzione main
# • Chiedere i dati all'utente
# • Mostrare il risultato

def recursive_pow(base: float, exp: float) -> float:
    if exp == 0: return 1.0
    elif exp == 1: return base
    return base * recursive_pow(base, exp - 1)

def main():
    base = float(input("insert a value for the base: "))
    exp = float(input("insert a value for the exponent: "))

    result = recursive_pow(base, exp)
    print(f"il risultato di {base}^{exp} è {result}")

if __name__ == "__main__": main()