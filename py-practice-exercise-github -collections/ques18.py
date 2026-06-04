s = input("ENter the string: ")
L = []
temp = ''

for i in s:
    if i != ' ':
        temp += i
    
    else:
        L.append(temp)
        temp = ''

L.append(temp)
print(L)