def find_mode(arr):

    frequent_dict = {}

    for i in arr:
        frequent_dict[i] = frequent_dict.get(i, 0) + 1

    mode = max(frequent_dict, key=frequent_dict.get)
    return mode






data = [1, 3, 3, 2, 1, 1, 4, 3, 3]
result = find_mode(data)

print(f"The dictionary of items is: {data}")
print(f"The mode is {result}")