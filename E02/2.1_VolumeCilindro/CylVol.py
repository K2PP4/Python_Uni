from math import pi

def cylinderVolume(radius: float, height: float) -> float :
    if radius < 0:
        raise ValueError("cannot calculate volume if radius is negative")
    elif height < 0:
        raise ValueError("cannot calculate volume if height is negative")

    return pi*(radius**2)*height

def main():
    r = float(input("insert the radius value"))
    h = float(input("insert the height value"))
    cylinder_volume = cylinderVolume(r, h)
    print("the cylinder's volume is " + str(cylinder_volume))