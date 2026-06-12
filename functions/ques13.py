def recur_factorial(n):
    if n<=1:
        return 1
    
    else:
        return n * recur_factorial(n-1)
    
num = int(input("Enter a non-negative integer: "))
print(f"The factorial of {num} is {recur_factorial(num)}")