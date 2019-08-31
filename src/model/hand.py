from model.card import Card

class Hand:
    __BLACKJACK = 21
    __FACE_VALUE = 10
    __ACE_VALUE_HIGH = 11
    __ACE_VALUE_LOW = 1

    def __init__(self, dealer: bool = False):
        self.__dealer = dealer
        self.__cards = []
        self.__value = 0
    
    def add_card(self, card: Card):
        self.__cards.append(card)
    
    def calculate_value(self):
        self.__value = 0
        ace_count = 0
        for card in self.__cards:
            if card.value.isnumeric():
                self.__value += int(card.value)
            else:
                if card.value == "A":
                    ace_count += 1
                    self.__value += Hand.__ACE_VALUE_HIGH
                else:
                    self.__value += Hand.__FACE_VALUE
        
        if ace_count > 0 and self.__value > Hand.__BLACKJACK:
            for dummy_variable in range(ace_count):
                if self.__value > 21:
                    self.__value -= 10
    
    def get_value(self):
        self.calculate_value()
        return self.__value
    
    def display_hand(self):
        if self.__dealer:
            print("Card #1: hidden")
            print(f"Card #2: {self.__cards[1]}")
        else:
            for index, card in enumerate(self.__cards):
                print(f"Card #{index + 1}: {card}")
            print("hand value: ", self.get_value())