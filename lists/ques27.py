def extract_nth(lst, n):

    return lst[::n]


my_list = ['a','b','c','d','e','f','g','h','i']
n_val = 3

result = extract_nth(my_list, n_val)

print(result)