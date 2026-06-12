initial_list = [100, 50, 400, 500]

initial_list[1] = 200
print(f"The changed second third element {initial_list}")
initial_list.append(600)
print(f"The updated list after appending 600 {initial_list}")
initial_list.insert(2,300)
print(f"The updated list after insertion is {initial_list}")
initial_list.remove(600)
print(f"The updated list after the removal of 600 is {initial_list}")
initial_list.pop(0)
print(f"The updated list after the removal of element at 0 index is {initial_list}")

