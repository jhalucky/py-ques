# User function Template for python3
# Back-end complete function Template for Python 3

a = int(input())
b = int(input())

########### Write your code below ###############
import math
lcm = abs(a * b) // math.gcd(a, b)
########### Write your code above ###############

print(lcm)