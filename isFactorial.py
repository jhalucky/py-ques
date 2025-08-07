
def is_factorial_number(x):
    if x == 1:
        return True  # 0! and 1! are both 1
    
    fact = 1
    n = 1
    while fact < x:
        n += 1
        fact *= n
    
    return fact == x

# # Test cases
# nums = [1, 2, 3, 6, 24, 25, 120, 150, 720, 5040, 10000]
# for num in nums:
#     result = is_factorial_number(num)
#     print(f"{num}: {'Yes' if result else 'No'}")



print(is_factorial_number(10))