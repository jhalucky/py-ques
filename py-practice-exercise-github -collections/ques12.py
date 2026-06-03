# palindrome

# str = input("Enter the string to check if it palindrome or not: ")

# if str == str[::-1]:
#     print("String is palindrome")
# else:
#     print("Not palindrome")



def palindrome_check(string):

    original_str = string
    reversed_str = original_str[::-1]
    
    if original_str == reversed_str:
        print("String is palindrome")

    else:
        print("Not palindrome!")


palindrome_check("1234567")
palindrome_check("madam")