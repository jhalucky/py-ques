num = int(input("Enter a number between the range 0-999: "))

# use nested-if statements

if num < 0 or num > 999:
    print("Invalid Entry. Valid range was between 0-999.")

else:
    if num < 10:
        print("Single digit number is entered.")

    else:
        if num < 100:
            print("Two digit number is entered.")

        else:
            print("Three digit number is entered.")