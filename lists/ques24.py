# Find the first occurrence of a specific value in a list and replace it with a new value.


new_list = [5,10,15,20,25,30]
target_value = int(input("Enter the target value: "))
replacement = int(input("Enter the replacement: "))



if target_value in new_list:
    target_index = new_list.index(target_value)
    new_list[target_index] = replacement

else:
    print(f"{target_value} not found in {new_list}")


print(new_list)





