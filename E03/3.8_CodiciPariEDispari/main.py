'''
Per ogni riga di testo inserita dall'utente, stampare:

    Il numero delle minuscole con codice Unicode dispari: a, c, e…
    Il numero delle minuscole con codice Unicode pari: b, d, f…
    Es. "Python": 3 minuscole con codice pari, 2 con codice dispari

Il programma si interrompe quando l'utente inserisce una riga vuota
Mostrare infine anche i conteggi complessivi

    Minuscole con codice dispari
    Minuscole con codice pari
    Numero di righe non vuote
'''

def isEven(ch: chr) -> bool:
    if ord(ch) % 2 == 0: return True
    else: return False

def countLetters(line: str) -> (int, int):
    countEven = 0
    countOdds = 0

    for ch in line:
        if ch >= 'a' and ch <= 'z':
            if isEven(ch): countEven += 1
            else: countOdds += 1

    return (countEven, countOdds)

def main():
    line = " "

    while line != "":
        line = input("insert a new line: ")
        if line != "": 
            letNums = countLetters(line)
            print(f"Number of lowercase even chars: {letNums[0]} \nNumber of lowercase odd chars: {letNums[1]}")

if __name__ == "__main__":
    main()