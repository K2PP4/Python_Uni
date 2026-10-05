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

    print("Average value: " + str(avg))
    print("Values bigger or equal to the average: " + str(higherAvg))
    print("Values smaller than the average: " + str(underAvg))

main()