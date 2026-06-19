def remove_neg_inplace(lst):

    for i in range(len(lst)-1, -1, -1):
        if lst[i] < 0:
            del lst[i]

my_nums = [10,20,-1,5,100,99,-3,9,0,-88]
print(f"Original list: {my_nums}")
remove_neg_inplace(my_nums)
print(f"List after deletion : {my_nums}")