starting_temperature = int(input("input which tempeture you want to convert, celsius (1), fahrenheit (2), kelvin (3): "))
end_temperature = int(input("input to which tempeture you want to convert, celsius (1), fahrenheit (2), kelvin (3): "))

if starting_temperature == 1:
    if end_temperature == 1:
        celsius = float(input("how hot/cold is it?: "))
        print(f"its", celsius,"°C")
    elif end_temperature == 2:
        celsius = float(input("how hot/cold is it?: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"its", fahrenheit,"°F")
    elif end_temperature == 3:
        celsius = float(input("how hot/cold is it?: "))
        kelvin = celsius + 273.15
        print(f"its", kelvin,"K")
    else:
        print("input a valid number")
elif starting_temperature == 2:
    if end_temperature == 1:
        fahrenheit = float(input("how hot/cold is it?: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"its", celsius,"°C")
    elif end_temperature == 2:
        fahrenheit = float(input("how hot/cold is it?: "))
        print(f"its", fahrenheit,"°F")
    elif end_temperature == 3:
        fahrenheit = float(input("how hot/cold is it?: "))
        kelvin = (fahrenheit - 32) * 5/9 + 273.15
        print(f"its", kelvin,"K")
    else:
        print("input a valid number")
elif starting_temperature == 3:
    if end_temperature == 1:
        kelvin = float(input("how hot/cold is it?: "))
        celsius = kelvin - 273.15
        print(f"its", celsius,"°C")
    elif end_temperature == 2:
        kelvin = float(input("how hot/cold is it?: "))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        print(f"its", fahrenheit,"°F")
    elif end_temperature == 3:
        kelvin = float(input("how hot/cold is it?: "))
        print(f"its", kelvin,"K")
    else:
        print("input a valid number")
else:
    print("input a valid number")
