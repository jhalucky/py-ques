string = input("Enter any string: ")

element = input("Enter element to check: ")

counter = 0



for i in string:
    if i == element:
        counter+=1

print(element,"is repeating",counter,"times")


