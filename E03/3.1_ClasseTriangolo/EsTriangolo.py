import math as mt

class Triangle:
    def __init__(self, leg1, leg2, leg3):
        if leg1 <= 0 or leg2 <= 0 or leg3 <= 0:
            raise ValueError("All sides must be positive numbers.")
        if (leg1 + leg2 <= leg3) or (leg1 + leg3 <= leg2) or (leg2 + leg3 <= leg1):
            raise ValueError("The sum of any two sides must be greater than the third side.")
        self.leg1 = leg1
        self.leg2 = leg2
        self.leg3 = leg3

    def getPerimeter(self):
        return self.leg1 + self.leg2 + self.leg3

    def getArea(self):
        s = self.getPerimeter() / 2
        area = mt.sqrt(s * (s - self.leg1) * (s - self.leg2) * (s - self.leg3)) # Formula di Erone per l'area 
        return area

def main():
    try:
        leg1 = float(input("Enter the length of the first side: "))
        leg2 = float(input("Enter the length of the second side: "))
        leg3 = float(input("Enter the length of the third side: "))

        triangle = Triangle(leg1, leg2, leg3)

        perimeter = triangle.getPerimeter()
        area = triangle.getArea()

        print(f"The perimeter of the triangle is: {perimeter}")
        print(f"The area of the triangle is: {area}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

