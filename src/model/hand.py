from model.card import Card

class Hand:
    def __init__(self, dealer: bool = False):
        self.__dealer = dealer
        self.__cards = []
        self.__value = 0
    
    def add_card(self, card: Card):
        self.__cards.append(card)