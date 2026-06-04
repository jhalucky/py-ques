# string = input("Enter the string: ")

# n = input("ENter term: ")

# result = ''

# for i in string:
#     if i != n:
#         result += i
        


# print(string)
# print(result)


# palindrome or not

original_string = input("Enter the string: ")

reversed_string = original_string[::-1]

if original_string == reversed_string:
    print("It is palindrome!")

else:
    print("Not palindrome!")