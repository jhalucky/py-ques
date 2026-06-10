text = input("Enter a string: ")

text2 = text.split()
capitalized = []
for i in text2:
    capitalized.append(i.capitalize())

print(" ".join(capitalized))
