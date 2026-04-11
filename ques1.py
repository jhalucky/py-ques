number = int(input("Enter a number between 0-999: "))

if number < 0:
    print("Invalid number. Please enter a valid digit.")

elif number < 10:
    print("Single digit number.")

elif number < 100:
    print("Two digit number is entered.")

elif number <= 999:
    print("Three digit number is entered.")

else:
    print("valid entry was between range 0-999")

