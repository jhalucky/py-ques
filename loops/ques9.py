items = ["apple", "mango", "banana", "litchi", "pomegrante","apple"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate item:", item)
        break
    unique_item.add(item)
print("Unique items:", unique_item)