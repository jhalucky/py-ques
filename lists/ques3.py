sum = 0

numbers = [10, 20, 30, 40, 50]
# here we could have use sum() function but just to practice loops i did this ow it depends on you how you want to do
for i in numbers:
    sum+=i

average = sum/len(numbers)

print(f"the sum of all integers is {sum}")
print(f"The average is {average}")