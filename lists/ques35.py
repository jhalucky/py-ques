def specific_concat(lst1, lst2):
    return [x + y for x in lst1 for y in lst2]

lst1 = ["hello ", "fuck "]
lst2 = ["sir", "off"]

concated_lst = specific_concat(lst1, lst2)
print(concated_lst)


