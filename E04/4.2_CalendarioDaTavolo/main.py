DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

def printCal(startNum: int, lastDay: int) -> None:
    for i in range(0, lastDay + startNum):
        if (i % 7 == 0): print('\n')
        if (i - startNum) >= 0:
            print(f"{i - startNum + 1}", end="\t")
        else: print("\t", end="")
    print() # zsh prints % if the command doesn't return a value with '\n' at the end.

def main():
    daysNum = int(input("insert the length of the month (range 28-31): "))
    if daysNum >= 27 and daysNum <= 31:
        firstDay = input("insert the first day of the month: ")
        if firstDay.lower() in DAYS:
            startnum = DAYS.index(firstDay.lower())
            printCal(startnum, daysNum)

if __name__ == "__main__":
    main()