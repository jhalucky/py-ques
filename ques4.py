# repeated addition


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

product = 0
count = num1

while count > 0:
    count = count - 1
    product = product + num2
print("The product of", num1, "and", num2, "is", product)