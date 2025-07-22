size = int(input()) #size of the wall

# using string multiplication
for i in range(size):
    print("*" * size)

# comment above working code before using below code

# without string multiplication
for i in range(size): #handles row
    for j in range(size): #print * per column
        print("*",end='')
    print()
    