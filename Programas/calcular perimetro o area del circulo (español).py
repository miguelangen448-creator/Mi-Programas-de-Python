import math

choose = int(input("¿Quieres calcular el perimetro del circulo (escribe 1) o el area de un circulo (escribe 2)?: "))

if choose == 1:
    diameter = int(input("escribe el diametro: "))
    
    perimeter = diameter * math.pi
    print(f"el perimetro del circulo es", perimeter)
elif choose == 2:
    radious = int(input("escribe el radio: "))
    
    area = radious ** 2 * math.pi
    print(f"el area del circulo es", area)
