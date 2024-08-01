from tools import deal_card, calculate_score, message
from clear import clear_console
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer = []
player = []

def black_jack():
    """The black_jack() function initiates the game program. It has a reset functionality after a round of play is completed if user input is Y/y"""
    while True:
        clear_console()
        dealer = []
        player = []

        deal_card(dealer, 1, cards)
        deal_card(player, 2, cards)

        dealer_sum = calculate_score(dealer)
        player_sum = calculate_score(player)

        while True:
            print(F"{logo}\n🂡 Dealer First Card: {dealer[0]}\n🂡 Player Hand: {player} Score: {player_sum}")

            if player_sum > 21:
                if 11 in player:
                    player.remove(11)
                    player.append(1)
                    player_sum = calculate_score(player)
                    print(F"Replaced card 11 with 1\n🂡 New Player Hand: {player} Score: {player_sum}")
                else:
                    print(F"BUST! You are over 21 with {player_sum} - 😭 Dealer Wins 😭")
                    break

            if player_sum == 21 and len(player) == 2 and len(dealer) == 1:
                print(F"BLACKJACK! 😎 Player wins with {player_sum} 😎")
                break

            player_turn = input("Hit(H) or Stand(S)?:\n").lower()
            if player_turn == "s":
                #While loop to ensure that Dealer "HITS" and receives a card while their total score is below 17 (Blackjack rules: Dealer MUST hit as many times as needed if their score is below 17, if it's 17 or over then Dealer will "STAND")
                while dealer_sum < 17:
                    deal_card(dealer, 1, cards)
                    dealer_sum = calculate_score(dealer)
                    print(F"DEALER HAND PROGRESSION: {dealer}")
                    #Here, we ensure that should dealer_sum be greater than 21 during the while loop AND 11 is appended to the hand from the ABOVE execution --> Then we remove 11 and replace with 1 (NOTE: Important to re-calculate to change dealer_sum and continue wihtin while loop)
                    if dealer_sum > 21 and 11 in dealer:
                        dealer.remove(11)
                        dealer.append(1)
                        dealer_sum = calculate_score(dealer)
                        print(F"Replaced card 11 with 1\n🂡 New Dealer Hand: {dealer} Score: {dealer_sum}")
                        
                if player_sum == 21 and dealer_sum != 21:
                    message(dealer, dealer_sum, player, player_sum)
                    print(F"😎 Player Wins! 😎")
                elif player_sum > dealer_sum and dealer_sum != 21 and player_sum < 21:
                    message(dealer, dealer_sum, player, player_sum)
                    print(F"😎 Player wins! 😎")
                elif dealer_sum > 21:
                    message(dealer, dealer_sum, player, player_sum)
                    print(F"😎 Player wins! 😎")
                elif player_sum == 21 and dealer_sum == 21:
                    message(dealer, dealer_sum, player, player_sum)
                    print(F"🤔 It's a draw 🤔")
                elif player_sum == dealer_sum:
                    message(dealer, dealer_sum, player, player_sum)
                    print(F"🤔 It's a draw 🤔")
                else:
                    message(dealer, dealer_sum, player, player_sum)
                    print(F"😭 Dealer wins 😭")
                break
            elif player_turn == "h":
                clear_console()
                deal_card(player, 1, cards)
                player_sum = calculate_score(player)
            else:
                clear_console()
                print("---- Please provide a valid input ----")

        reset = input("Would you like to play again? - Type Y for yes or anything else to exit:\n").lower()
        if reset != "y":
            print("Exiting...")
            return

black_jack()
