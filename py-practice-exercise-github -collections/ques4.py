# using for loop and range function

s = input("Enter the string: ")

# for i in range(0, len(s)-1, 2):
#     print(s[i])


# using slicing

even_chars = s[0::2]

for i in even_chars:
    print(i)

