import random

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"
    


class Deck:

    def __init__(self):

        suits = ["Hearts", "diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        self.cards = []

        for suit in suits:  # runs 4 times cuz we have 4 suits
            for value in values: # runs 13 times for each suit
                self.cards.append(Card(suit, value)) #and therefore it results in 52 pairs of suit, value or in short 52 cards. 


        random.shuffle(self.cards) #shuffling the cards

    def deal(self):
        if len(self.cards) == 0:
            return "No cards Left"
        return self.cards.pop() #pops out a last card from self.cards[] and returns it 
    

    def __str__(self):
        return f"No of cards remaining in the Deck- {len(self.cards)}"
    




deck = Deck()
# print(deck) here if we print deck it will show 52 cards every time
    

card = deck.deal()
print(card)
print(deck) # and here it will show remaining number of cards remaining in the list after popping out the last card