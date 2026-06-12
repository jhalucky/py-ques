sum = 0

numbers = [10, 20, 30, 40, 50]
for i in numbers:
    sum+=i

average = sum/len(numbers)

print(f"the sum of all integers is {sum}")
print(f"The average is {average}")