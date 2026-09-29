from math import sqrt

def hypotenuse(a: float, b: float) -> float:
    '''
    Return the hypotenuse of a right triangle,
    given both its legs (catheti).
    '''
    c = sqrt(a ** 2 + b ** 2)
    return c

def main():
    side1 = float(input("insert 1st side: "))
    side2 = float(input("insert 2nd side: "))
    side3 = hypotenuse(side1, side2)

    print("3rd side = " + str(side3))

main()