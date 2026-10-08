from classes.mainClasses import Car

def main():
    macchine = []
    make = ""

    while make.lower() != "exit":
        macchina = Car()
        print(f"Car {len(macchine) +1}: [enter 'exit' to stop adding cars]")
        make = input("Enter the make: ")
        if make.lower() != "exit":
            model = input("Enter the model: ")
            year = input("Enter the year: ")
            nickname = input("Enter a nickname (optional): ")
            macchina.setValues(make, model, year, nickname)
            print(f"Car {len(macchine) +1} added:\n  {macchina}")
            macchine.append(macchina)

    if len(macchine) > 0:
        print("\nCar details:")
        for i, macchina in enumerate(macchine):
            print(f"Car {i + 1}: {macchina}")

if __name__ == "__main__":
    main()
