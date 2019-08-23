import random

class Card:
    def __init__(self, suit, value):
        self.__suit = suit
        self.__value = value
    
    def __repr__(self):
        return " of ".join((self.__value, self.__suit))