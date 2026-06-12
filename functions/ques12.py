global_var = 10

def modify_value():
    global global_var
    global_var = 20

print(f"Intial value: {global_var}")
modify_value()
print(f"Modified value: {global_var}")

