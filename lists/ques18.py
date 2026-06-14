# Practice Problem: Delete every instance of a specific value from a list.


input_list = [10, 20, 30, 50, 60, 90, 20, 10, 40, 50, 60, 5, 15, 20, 30]

target = int(input("Enter target no.: "))




# using loop

# for i in input_list:
#     if i!=target:
#         new_list.append(i)

# using list comprehension
new_list = [i for i in input_list if i!=target]
print(f"Cleaned list: {new_list}")
