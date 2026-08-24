import math

choose = int(input("do you want to calculate the perimeter of the circle (type 1) or the area of a circle (type 2)?: "))

if choose == 1:
    diameter = int(input("input the diameter: "))
    
    perimeter = diameter * math.pi
    print(f"the perimeter of the circle is", perimeter)
elif choose == 2:
    radious = int(input("input the radious: "))
    
    area = radious ** 2 * math.pi
    print(f"the area of the circle is", area)
