import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer = []
player = []

dealer_sum = 0
player_sum = 0

#Deal ONE Random Card Function
def deal_card(user, times):
    """The deal_card() function generates one or two random cards, which is determined by the second parameter times. It returns"""
    if times == 1:
        for n in range(0, 1):
            card = random.choice(cards)
            user.append(card)
    elif times == 2:
        for n in range(0, 2):
            card = random.choice(cards)
            user.append(card)
    return

#Initial Cards
deal_card(dealer, 2)
deal_card(player, 2)

#Calculate Score Function
def calculate_score(hand):
    score = 0
    for c in hand:
        score += c
    return score

#Initial Score Calculations
dealer_sum = calculate_score(dealer)
player_sum = calculate_score(player)

while True:

    print(F"Dealer - Hand: {dealer} Score: {dealer_sum}")
    print(F"Player - Hand: {player} Score: {player_sum}")

    if player_sum > 21:
        print(F"You are over 21 with {player_sum} - Dealer Wins")
        break

    player_turn = input("Hit(H) or Stand(S)?:\n").lower()
    if player_turn == "s":
        if player_sum == 21:
            print(F"Player Wins with {player_sum}")
        elif player_sum > dealer_sum and dealer_sum != 21 and player_sum < 21:
            print(F"Player wins with {player_sum} over Dealer with {dealer_sum}")
        elif dealer_sum > 21:
            print(F"Player wins with {player_sum}. Dealer went over 21 with {dealer_sum}")
        elif player_sum == 21 and dealer_sum == 21:
            print(F"It's a draw. Player has {player_sum} and Dealer has {dealer_sum}")
        else:
            print(F"Dealer wins with {dealer_sum} over Player with {player_sum}")
        break
    elif player_turn == "h":
        deal_card(player, 1)
        player_sum = calculate_score(player)

