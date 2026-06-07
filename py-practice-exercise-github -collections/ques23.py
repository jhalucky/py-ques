# check palindrome or not

# to reverse a string

# def palindrome(str):

#     original_str = str
#     reversed_str = original_str[::-1]

#     if original_str == reversed_str:
#         print("it is palindrome!")

#     else:
#         print("Not palindrome")



# to reverse a number

def palindrome(number):


    original_num = number
    reversed_num = 0

    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number = number // 10

    if original_num == reversed_num:
        print("Its palindrome!")

    else:
        print("it's not")


palindrome(121)
palindrome(34567788903)
palindrome(00000)
palindrome(1234567)
