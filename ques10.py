distance = int(input("Enter the distance in kilometers: "))


if distance < 3:
    print("Walk")

elif distance < 15:
    print("Bike")

else:
    print("Car")