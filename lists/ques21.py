# Practice Problem: Given a list of integers, use list comprehension to create a new list that contains only the even numbers from the original list.


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_list = [i for i in input_list if i % 2 == 0]

print(filtered_list)
