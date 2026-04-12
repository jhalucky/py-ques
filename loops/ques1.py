numbers = [1, -2, 3, -4, 5,6, -7, -8, 9, 10]
positive_num_count = 0
negative_num_count = 0

for i in numbers:
    # print(i, end=" ")
    if i > 0:
        positive_num_count += 1
    
    else:
        negative_num_count += 1

print("Number of positive integers: ", positive_num_count)
print("Number of negative integers: ", negative_num_count)
