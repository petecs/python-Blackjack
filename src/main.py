from model import Card
from model import Deck
from model import Hand
from controller import Game

def main():
    test_deck = Deck()
    test_deck.shuffle()
    #test_deck.print_deck()

    test_hand = Hand(True)
    test_hand.add_card(test_deck.deal_card())
    test_hand.add_card(test_deck.deal_card())
    test_hand.display_hand()

    Game()

main()