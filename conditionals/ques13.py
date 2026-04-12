pet = input("Enter the pet: ")
pet_age = int(input("Enter the age of the pet: "))

if pet == "Dog":
    if pet_age < 2:
        food = "Puppy food"
        print(food)

    else:
        food = "Dog food"
        print(food)

if pet == "Cat":
    if pet_age > 5:
        food = "Senior Cat food"
        print(food)

    else:
        food = "Junior Cat food"
        print(food)


