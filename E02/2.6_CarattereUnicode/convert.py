def main():
    inputNr = 0
    while (inputNr != "") :
        inputNr = input("insert a number please: ")
        if (inputNr != "") :
            character = chr(int(inputNr))
            print("the value is: " + character)

main()