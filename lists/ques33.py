def get_set_diff(lst1, lst2):
    excluded = set(lst2)

    return [i for i in lst1 if i not in excluded]



a = [1,2,3,4,5,6]
b = [2,4,6]

result = get_set_diff(a,b)

print(f"List A: {a}")
print(f"List B: {b}")
print(f"Elements in A but not in B: {result}")
