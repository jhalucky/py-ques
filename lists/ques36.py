twod_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# flat_list = [item for sublist in twod_list for item in sublist]


flat_list = []

for sublist in twod_list:
    flat_list.extend(sublist)

    
print(flat_list)