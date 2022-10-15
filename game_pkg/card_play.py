import random
cards = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
d = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,
           'J':10, 'Q':10, 'K':10, 'A':11}

def new_hand():
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    hand = [card1, card2]
    return hand
    
def total(hand):
    total = 0
    for i in hand:
        total = total + d[i]
    if "A" in hand and total >= 22:
        total -= 10
    return total

def new_card():
    new_card = random.choice(cards)
    hand = new_card
    return hand

def repeat(username):
    while True:
        again = input("\nPlay again (Y/N): ")
        if again == "Y" or again == "y":
            print("\n Good luck,", username, "!")
            break
        elif again == "N" or again =="n":
            print("Thanks for playing,", username, "!")
            exit()
        else:
            print("Invalid selection")
