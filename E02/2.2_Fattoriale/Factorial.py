def factorial(n: int) :
    if n < 0:
        raise ValueError("please insert a positive number")
    if n == 0: return 1

    res = 1

    for i in range(0, n):
        res *= i+1

    return res

def main():
    num = int(input("insert a number to calculate its factorial: "))
    result = factorial(num)

    print("the value's factorial is " + str(result))

main()