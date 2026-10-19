import math

class Exp():
    def __init__(self, a: float, b: float, c: float):
        if a == 0 or b == 0:
            raise ValueError("Can't be an exponential if args a OR b are equal to 0.")
        else:
            self._a = a
            self._b = b
            self._c = c

    def predict(self, x: float) -> float:
        return (self._a * math.e ** (self._b * x)) + self._c

def main():
    
    param_a = float(input("insert value of param. A: "))
    param_b = float(input("insert value of param. B: "))
    param_c = float(input("insert value of param. C: "))
    exp = Exp(param_a, param_b, param_c)

    x = 0

    while x != "":
        x = input("insert X: ")
        if x != "":
            x = float(x)
            print(f"value of Y in X: {exp.predict(x)}")
        
if __name__ == "__main__":
    main()