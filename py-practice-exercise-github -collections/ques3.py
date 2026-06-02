prev_num = 0

for i in range(10):
    x_sum = prev_num + i
    prev_num = i

    print("Current num:",i, "Previous num:",prev_num, "Sum:",x_sum)