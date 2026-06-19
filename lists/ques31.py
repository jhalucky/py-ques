def check_sorted(lst):
    if lst == sorted(lst):
        return True
    else:
        return False
    

lst = [10, 20, 30, 25, 40]
print(check_sorted(lst))