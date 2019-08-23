import random
from model.card import Card

class Deck:
    def __init__(self):
        self.__cards = []

        self.__suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        self.__values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        
        for suit in self.__suits:
            for value in self.__values:
                self.__cards.append(Card(suit, value))
        
    def shuffle(self):
        if len(self.__cards) > 1:
            random.shuffle(self.__cards)
    
    def deal_card(self) -> Card:
        if len(self.__cards) > 1:
            return self.__cards.pop(0)
    
    def print_deck(self):
        if len(self.__cards) == 0:
            print("deck is empty")
            return
        
        for num in range(len(self.__cards)):
            print(f"Card #{num +1}: {self.__cards[num]}")