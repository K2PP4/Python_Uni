def main():
    for y in range(0, 5):
        for x in range(0, 5):
            print(f"   {abs(x-y)}", end="")
        print("\n")

if __name__ == "__main__":
    main()