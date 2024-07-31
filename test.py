import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer = []
for n in range(0, 2):
    card = random.choice(cards)
    dealer.append(card)
# print(dealer[0])
print(dealer)

player = []
for n in range(0, 2):
    card = random.choice(cards)
    player.append(card)
print(player)

player_turn = input("Hit(H) or Stand(S)?:\n").lower()
if player_turn == "s":
    player_sum = 0
    dealer_sum = 0
    for c in player:
        player_sum += c
    for c in dealer:
        dealer_sum += c
    
    if player_sum == 21:
        print(F"Player Wins with {player_sum}")
    elif player_sum > dealer_sum and dealer_sum != 21:
        print(F"Player wins with {player_sum} over Dealer with {dealer_sum}")
    elif dealer_sum > 21:
        print(F"Player wins with {player_sum}. Dealer went over 21 with {dealer_sum}")
    elif player_sum == 21 and dealer_sum == 21:
        print(F"It's a draw. Player has {player_sum} and Dealer has {dealer_sum}")
    else:
        print(F"Dealer wins with {dealer_sum} over Player with {player_sum}")

