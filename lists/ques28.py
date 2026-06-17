def is_palindrome(lst):

    reversed_lst = lst[::-1]

    return lst == reversed_lst
    
    
    
lst1 = [1,2,3,2,1]
lst2 = [2,3,4,5,6]

print(f"{lst1} is palindrome? {is_palindrome(lst1)}")
print(f"{lst2} is palindrome? {is_palindrome(lst2)}")
