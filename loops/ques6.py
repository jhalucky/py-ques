n = int(input("Enter the number: "))

factorial = 1

# using for loop

# for i in range(1, n+1):
#     factorial *= i
# print(factorial)

# using while loop

while n > 0:
    factorial *= n
    n -= 1

print(factorial)