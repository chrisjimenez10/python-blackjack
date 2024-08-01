import random

#Deal ONE Random Card Function
def deal_card(user, times, arr):
    """The deal_card() function generates one or two random cards, which is determined by the second parameter"""
    if times == 1:
        for n in range(0, 1):
            card = random.choice(arr)
            user.append(card)
    elif times == 2:
        for n in range(0, 2):
            card = random.choice(arr)
            user.append(card)
    return

#Calculate Score Function
def calculate_score(hand):
    score = 0
    for card in hand:
        score += card
    return score

#Message Function
def message(user1, score1, user2, score2):
    print(F"🂡 Dealer Hand: {user1} - Score: {score1}\n🂡 Player Hand: {user2} - Score: {score2}")