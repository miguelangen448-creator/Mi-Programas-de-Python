number = int(input("choose you initial number: "))
print("1 = +, 2= -, 3 = *, 4 = /")
operation = int(input("chose your operation: "))

if operation == 1:
	second_number = int(input("choose which number you would like to add: "))
	result = number + second_number
	print(f"{number} + {second_number} = {result}")

if operation == 2:
	second_number = int(input("choose which number would you like to rest: "))
	result = number - second_number
	print(f"{number} - {second_number} = {result}")

if operation == 3: 
	second_number = int(input("choose which number you would like to multiply: "))
	result = number * second_number
	print(f"{number} * {second_number} = {result}")

if operation == 4:
	second_number = int(input("choose which number you would like to dividide: "))
	result = number / second_number
	print(f"{number} / {second_number} = {result}")