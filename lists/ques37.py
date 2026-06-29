def cumulative_sum(nums):

    total = 0
    sums = []

    for i in nums:

        total+=i
        sums.append(total)
    
    return sums   


numbers = [10,20,30,40]
result = cumulative_sum(numbers)

print(result)