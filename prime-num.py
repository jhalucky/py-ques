import math
n = int(input())

# Your code here
if n <= 1: #number should be greater than 1
    print("False") 
    
for i in range(2, int(math.sqrt(n)) + 1):  # here we check the till the square root of n
    if n % i == 0:
        print("False")
else:
    print("True")