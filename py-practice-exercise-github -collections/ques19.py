string = input("ENter a string: ")

words = string.split()
L =[]

for i in words:
    # print(i.capitalize(), end=" ") # this will capitalize the first letter of each word and print it
    L.append(i[0].upper() + i[1:].lower())
print(' '.join(L))