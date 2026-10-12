def sum_digits(n: int) -> int:
    sm = 0
    while n > 0:
        sm += n % 10
        n //= 10
    return sm

def main():
    n = int(input("inserire un numero: "))
    while (len(str(n)) != 1):
        n = sum_digits(n)
        print(f"Summed digits: {n}")

if __name__ == "__main__":
    main()