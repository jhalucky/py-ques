def find_second_largest(nums):

    unique_list = list(set(nums))

    if len(unique_list) < 2:
        return None
    
    unique_list.sort(reverse=True)

    return unique_list[1]





numbers = [12, 35, 34, 1, 10, 35, 1, 10]

print(find_second_largest(numbers))
