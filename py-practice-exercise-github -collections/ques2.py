# Solution 1


# x = int(input("Enter the value for x: "))

# fact = 1
# i = 1
# while i <= x:
#     fact *= i
#     i+=1

# print(fact)

# Solution 2 - using function


def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

x=int(input())
print(fact(x))
