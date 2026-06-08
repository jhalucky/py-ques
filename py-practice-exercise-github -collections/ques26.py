numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

even = []
odd = []

for i in numbers:
    if i%2 == 0:
        even.append(i)
    
    else:
        odd.append(i)


print(even)
print(odd)