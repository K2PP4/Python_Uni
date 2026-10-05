def count_groups(line: str) -> tuple:
    group1, group2 = 0,0

    line = line.upper()

    for letter in line:
        if letter >= 'A' and letter <= 'M':
            group1 += 1
        elif letter >= 'N' and letter <= 'Z':
            group2 += 1

    return (group1, group2)

def main():
    inputString = " "

    while(inputString != ""):
        inputString = str(input("insert a string: "))
        if inputString != "":
            letterNumbers = count_groups(inputString)
            
            print("Letters from A to M: " + str(letterNumbers[0]) + "\nLetters from N to Z: " + str(letterNumbers[1]))

main()