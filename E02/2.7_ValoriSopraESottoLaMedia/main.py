def main():
    inputNr = int(input("insert numbers: "))

    nrs = []
    
    while(inputNr != 0) :
        nrs.append(inputNr)
        inputNr = int(input("insert numbers: "))

    sum = 0
    nItems = 0

    for n in nrs:
        sum += n
        nItems += 1

    avg = sum / nItems

    underAvg = []
    higherAvg = []

    for n in nrs:
        if n >= avg:
            higherAvg.append(n)
        else:
            underAvg.append(n)

    print(f"Average value: {avg}")
    print(f"Values bigger or equal to the average: {higherAvg}")
    print(f"Values smaller than the average: {underAvg}")

main()