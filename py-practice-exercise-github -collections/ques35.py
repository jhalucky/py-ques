string = input("Enter the string: ")
contains_digit = False

for i in string:
    if i.isdigit():
        contains_digit = True
        break

print(f"The string '{string}' contains digits: {contains_digit}")
