from model import Card
from model import Deck

def main():
    test_card = Card("Ace", "10")
    print(test_card)
    test_deck = Deck()
    print(test_deck.cards)

main()