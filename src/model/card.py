class Card:
    def __init__(self, suit: str, value: str):
        self.__suit = suit
        self.__value = value
    
    @property
    def value(self):
        return self.__value
    
    def __repr__(self) -> str:
        return " of ".join((self.__value, self.__suit))