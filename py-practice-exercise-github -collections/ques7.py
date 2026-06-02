fact = 1
n = int(input("Enter number to calculate factorial: "))
i = 1
# using for loop
# for i in range(1,n+1):
#     fact*=i

# print(fact)


# using while loop
while i<=n:
    fact*=i
    i+=1
print(fact)