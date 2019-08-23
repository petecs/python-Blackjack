from model.card import Card

class Deck:
    def __init__(self):
        self.__suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        self.__values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        
        self.__cards = []
        self.cards = self.__cards

        for suit in self.__suits:
            for value in self.__values:
                self.__cards.append(Card(suit, value))