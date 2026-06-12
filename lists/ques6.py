even = 0
odd = 0

numbers = [10, 21, 4, 45, 66, 93, 11]

for i in numbers:
    if i % 2 == 0:
        even+=1

    else:
        odd+=1


print(f"Even: {even}\nOdd: {odd}")