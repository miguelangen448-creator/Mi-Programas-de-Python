print("3x + 1 generator")
n = int(input("choose you number: "))
while True:
    
    if n % 2 == 0:
        n = n/2
    else:
        n = n * 3 + 1
    print(n)
    input("continue?: ")
