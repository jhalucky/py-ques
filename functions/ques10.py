def find_largest(list_input):

    largest = list_input[0]
    for i in list_input:
        if i > largest:
            largest = i
    return largest


print(find_largest([10,9,11,23,4,5,6,90]))
