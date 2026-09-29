def trianglePerimeter (a: float, b: float, c: float) :
    if a > b + c or b > a + c or c > a + b:
        raise ValueError("Not a triangle !")
    return a + b + c

print("triangle perimeter: " + str(trianglePerimeter(23, 3, 2)))