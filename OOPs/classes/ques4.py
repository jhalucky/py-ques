import random

class Flashcard:

    def __init__(self, dict):
        fruit, color = random.choice(list(dict.items()))
        self.fruit = fruit
        self.color = color

        


    def display(self):
        print("Welcome to the Rapid Fire!")
        answer = input(f"What is the color of the {self.fruit}?")

        if answer.lower() == self.color.lower():
            print("Correct!")

        else:
            print("False! Try again.")

        wanna_play = int(input("Enter 0 if you want to play again: "))

        if wanna_play == 0:
            self.display()



fruits = {
    "Banana": "Yellow",
    "Strawberry": "Pink",
    "Apple": "Red",
    "Orange": "Orange",
    "Grapes": "Green",
    "Mango": "Yellow",
    "Blueberry": "Blue"
}
card1 = Flashcard(fruits)
card1.display()