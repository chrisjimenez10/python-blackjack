import random
from clear import clear_console
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer = []
player = []

#Deal ONE Random Card Function
def deal_card(user, times):
    """The deal_card() function generates one or two random cards, which is determined by the second parameter"""
    if times == 1:
        for n in range(0, 1):
            card = random.choice(cards)
            user.append(card)
    elif times == 2:
        for n in range(0, 2):
            card = random.choice(cards)
            user.append(card)
    return

#Calculate Score Function
def calculate_score(hand):
    score = 0
    for c in hand:
        score += c
    return score

#Message Function
def message(user1, score1, user2, score2):
    print(F"Dealer Hand: {user1} - Score: {score1}\nPlayer Hand: {user2} - Score: {score2}")

def black_jack():
    """The black_jack() function initiates the game program. It has a reset functionality after a round of play is completed if user input is Y/y"""
    while True:
        clear_console()
        dealer = []
        player = []

        deal_card(dealer, 2)
        deal_card(player, 2)

        dealer_sum = calculate_score(dealer)
        player_sum = calculate_score(player)

        while True:
            print(logo)
            print(F"Dealer First Card: {dealer[0]}")
            print(F"Player Hand: {player} Score: {player_sum}")

            if player_sum > 21:
                print(F"BUST! You are over 21 with {player_sum} - 😭 Dealer Wins 😭")
                break

            player_turn = input("Hit(H) or Stand(S)?:\n").lower()
            if player_turn == "s":
                #While loop to ensure that Dealer "HITS" and receives a card while their total score is below 17 (Blackjack rules: Dealer MUST hit as many times as needed if their score is below 17, if it's 17 or over then Dealer will "STAND")
                while dealer_sum < 17:
                    deal_card(dealer, 1)
                    dealer_sum = calculate_score(dealer)

                if player_sum == 21:
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
                deal_card(player, 1)
                player_sum = calculate_score(player)
            else:
                clear_console()
                print("Please provide a valid input")

        reset = input("Would you like to play again? - Type Y for yes or anything else to exit:\n").lower()
        if reset != "y":
            print("Exiting...")
            return

black_jack()