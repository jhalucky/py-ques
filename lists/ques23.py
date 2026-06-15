# Problem: Find a specific item in a list and insert a new item immediately after it

list1 = [10,20,30,40,50]
new_val = int(input("Enter new val: "))

target = int(input("Enter the target integer: "))

index = list1.index(target)

list1.insert(index+1, new_val)
print(list1)