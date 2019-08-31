from model.deck import Deck
from model.hand import Hand

class Game:
    __BLACKJACK = 21
    __DEALER_STANDS = 17
    
    def __init__(self):
        print()

        playing = True

        while playing:
            self.__deck = Deck()
            self.__deck.shuffle()

            self.__player_hand = Hand()
            self.__dealer_hand = Hand(dealer = True)

            self.__deal_initial_cards()
            self.__display_hands()
            print()

            game_over = False
            did_initial_blackjack_check = False

            while not game_over:
                if not did_initial_blackjack_check:
                    did_initial_blackjack_check = True

                    initial_blackjack = self.__check_for_initial_blackjack()
                    
                    if initial_blackjack:
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
                
                game_over = True
            
            if not initial_blackjack:
                self.__display_final_result()

            playing = self.__ask_to_play_again()
        
        print()



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
            print("The player and dealer both have blackjack! Draw!\n")
        elif player_has_blackjack:
            print("You have blackjack! You win!\n")
        elif dealer_has_blackjack:
            print("Dealer reveals hand...")
            self.__dealer_hand.display_hand_no_hidden()
            print("Dealer has blackjack! Dealer wins!\n")
    
    def __player_plays(self):
        choice = ""
        while choice not in ["s", "stand"]:
            choice = input("Please choose [Hit / Stand]: ").lower()

            if choice not in ["h", "s", "hit", "stand"]:
                print("Error: please enter 'hit' or 'stand' or (H/S) only")
                continue
            
            if choice == "hit" or choice == "h":
                self.__player_hand.add_card(self.__deck.deal_card())
                self.__player_hand.display_hand()
            
                if self.__did_player_bust():
                    break
            
            print()

    def __did_player_bust(self):
        if self.__player_hand.get_value() > Game.__BLACKJACK:
            return True
        else:
            return False

    def __did_dealer_bust(self):
        if self.__dealer_hand.get_value() > Game.__BLACKJACK:
            return True
        else:
            return False  
    
    def __dealer_plays(self):
        while self.__dealer_hand.get_value() < Game.__DEALER_STANDS:
            print("Dealer hits!")
            self.__dealer_hand.add_card(self.__deck.deal_card())

            if self.__did_dealer_bust():
                break
        
        print("Dealer stands!\n")
    
    def __display_final_result(self):
        print("Final Results:\n")
        if self.__did_player_bust():
            print("You busted! You lost!\n")
            return
        if self.__did_dealer_bust():
            print("The dealer busted! You win!\n")
            return
        
        print("Your hand: ")
        self.__player_hand.display_hand_no_hidden()
        print("\nDealer's hand: ")
        self.__dealer_hand.display_hand_no_hidden()

        print(f"\nYour hand value: {self.__player_hand.get_value()}")
        print(f"Dealer's hand value: {self.__dealer_hand.get_value()}")

        if self.__player_hand.get_value() == self.__dealer_hand.get_value():
            print("\nYour hand is equal to the dealer's hand! Draw!")
        elif self.__player_hand.get_value() > self.__dealer_hand.get_value():
            print("\nYour hand beats the dealer's hand! You win!")
        else:
            print("\nThe dealer's hand beats your hand! You lose!")
        
        print()
    
    def __ask_to_play_again(self):
        choice = ""

        while choice not in ["yes", "y", "no", "n"]:
            choice = input("Do you wish to play again?: ").lower()

            if choice not in ["yes", "y", "no", "n"]:
                print("Error: enter 'yes', 'y','no', or 'n'")
        
        if choice in ["yes", "y"]:
            return True
        else:
            print("\nThanks for playing!")
            return False