data = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# cleaned_list = list(filter(None, data)) using filter function


cleaned_list = []

for i in data:
    if i != "":
        cleaned_list.append(i)

print(cleaned_list)