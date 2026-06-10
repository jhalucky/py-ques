with open("notes.txt", "w") as file:
    file.write("Hello! This is my first note.\n")
    file.write("Python file handling is very simple.\n")
    file.write("End of File!")

print("reading file...")
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
