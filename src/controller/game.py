from model.deck import Deck
from model.hand import Hand

class Game:
    __BLACKJACK = 21
    __DEALER_STANDS = 17
    def __init__(self):
        playing = True

        while playing:
            self.__deck = Deck()
            self.__deck.shuffle()

            self.__player_hand = Hand()
            self.__dealer_hand = Hand(dealer = True)

            self.__deal_initial_cards()
            self.__display_hands()

            game_over = False
            did_initial_blackjack_check = False

            while not game_over:
                if not did_initial_blackjack_check:
                    did_initial_blackjack_check = True
                    
                    if self.__check_for_initial_blackjack():
                        game_over = True
                        continue
                
                self.__player_plays()

                if self.__did_player_bust():
                    game_over = True
                    continue
                
                self.__dealer_plays()

                if self.__did_dealer_bust():
                    game_over = True
                    continue
            
            if self.__did_dealer_bust():
                pass


    def __deal_initial_cards(self):
        for dummy_variable in range(2):
            self.__player_hand.add_card(self.__deck.deal_card())
            self.__dealer_hand.add_card(self.__deck.deal_card())
    
    def __display_hands(self):
        print("Your hand:")
        self.__player_hand.display_hand()
        print()
        print("Dealer's hand:")
        self.__dealer_hand.display_hand()

    def __check_for_initial_blackjack(self):
        player_has_blackjack = False
        dealer_has_blackjack = False

        if self.__player_hand.get_value() == Game.__BLACKJACK:
            player_has_blackjack = True
        if self.__dealer_hand.get_value() == Game.__BLACKJACK:
            dealer_has_blackjack = True
        
        if player_has_blackjack or dealer_has_blackjack:
            self.__show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
            return True
        else:
            return False
    
    def __show_blackjack_results(self, player_has_blackjack: bool, dealer_has_blackjack: bool):
        if player_has_blackjack and dealer_has_blackjack:
            print("The player and dealer both have blackjack! Draw!")
        elif player_has_blackjack:
            print("You have blackjack! You win!")
        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins!")
    
    def __player_plays(self):
        choice = ""
        while choice not in ["s", "stay"]:
            choice = input("Please choose [Hit / Stay]").lower()

            if choice not in ["h", "s", "hit", "stay"]:
                print("Error: please enter 'hit' or 'stay' or (H/S) only")
                continue
            
            if choice == "hit" or choice == "h":
                self.__player_hand.add_card(self.__deck.deal_card())
                self.__player_hand.display_hand()
            
                if self.__did_player_bust():
                    break

    def __did_player_bust(self):
        if self.__player_hand.get_value > Game.__BLACKJACK:
            print("You busted! You lost!")
            return True
        else:
            return False

    def __did_dealer_bust(self):
        if self.__dealer_hand.get_value > Game.__BLACKJACK:
            print("The dealer busted! You win!")
            return True
        else:
            return False  
    
    def __dealer_plays(self):
        while self.__dealer_hand.get_value < Game.__DEALER_STANDS:
            self.__dealer_hand.add_card(self.__deck.deal_card())

            if self.__did_dealer_bust():
                break