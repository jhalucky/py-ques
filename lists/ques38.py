def rotate_left(lst, k):

    if not lst:
        return lst
    
    n = len(lst)
    k =  k % n

    return lst[k:] + lst[:k]



numbers = [1, 2, 3, 4, 5, 6]
shift = 7
result = rotate_left(numbers, shift)

print(f"Original: {numbers}")
print(f"Left Rotated by {shift}: {result}")

