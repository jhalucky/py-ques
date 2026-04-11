a = b = c = 0

for i in range(1,11):
    a = int(input("Enter the number 1: "))
    b = int(input("Enter the number 2: "))

    if b == 0:
        print("Division by zero not allowed. Abort!")
        break

    else:
        c=a/b
        print("Quotient: ",c)
print("Program Over!")