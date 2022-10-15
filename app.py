# Import packages needed and set up win/loss counter variables
import os
import time
from game_pkg.user import login, register
from game_pkg.homepage import start_game, show_homepage
from game_pkg.card_play import new_hand, total, new_card, repeat
player_won = 0
player_lost = 0
player_balance = 0
blackjack = False
act = ""

# Set functionality for login screen
database = {"admin": "password123"}
authorized_user = ""
while True:
    os.system('cls')
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to play.")
    else:
        print("Logged in as:", authorized_user)
    option = input("\nPlease choose an option: ")
    if option == "1":
        username = input("\nUsername: ")
        password = input("Password: ")
        authorized_user = login(database, username, password)
    if option == "2":
        username = input("Choose a username: ")
        password = input("Choose a password: ")
        authorized_user = register(database, username)
    if option == "3" and authorized_user != "":
        print("\nGood Luck,", authorized_user, "!")
        print("May the odds be forever in your favor.")
        break
    else:
        print("You must be logged in to play a game.")
        print("Please login or register.")

# Start of game
while True:
    os.system('cls')
    start_game()
    print(f"               {username}'s record: ")
    print("               W:", player_won, "     L:", player_lost)
    while True:
        if player_balance == 0:
            print(f"{username} has a balance of $", player_balance)
            deposit = input("\nHow much are you buying in? $")
            deposit = int(deposit)
            player_balance += deposit
        else:
            print("\nour new balance is: $", player_balance)
            break
    while True:
        try:
            wager = int(input("Place your bet: $"))
            break
        except:
            print("Invalid option. You must place a numerical bet.")
    while True:
        if wager > player_balance:
            print("\nYou don't have enough. Maximum bet allowed is: $", player_balance)
        elif wager <= 0:
            print("\nInvalid selection. You must place a bet to play.")
        else:
            break
    print("\nDealing cards. . .")
    time.sleep(1)
    my_hand = new_hand()
    dealer_hand = new_hand()
    dealer_total = total(dealer_hand)

    print("\nYour hand is: ", my_hand)
    print("Total:", total(my_hand))

    if total(dealer_hand) == 21 and total(my_hand) < 21:
        print("Dealer has Blackjack!")
        print("Dealer wins!")
        player_lost += 1

    elif total(my_hand) == 21:
        print(f"{username} has BlackJack")
        blackjack = True
    else:
        print("\nThe dealer is showing: ", dealer_hand[0])

    # Functionality for player action to hit or stand
    # TODO write logic for hands with Aces
    while True:
        if total(my_hand) == 21:
            break
        elif total(my_hand) < 21 and total(dealer_hand) < 21:
            act = input("\nHit or Stand? ")
        if act == "H" or act == "h":
            card = new_card()
            my_hand.append(card)
            print(f"\n{username} is drawing another card. . .")
            time.sleep(2)
            print("\nYour current hand is: ", my_hand)
            print("Total:", total(my_hand))
        if total(my_hand) > 21:
            print("Sorry, you busted!")
            player_lost += 1
            player_balance -= wager
            break
        if act == "S" or act == "s":
            break

    # Defines dealer action and shows hand with total points
    print("\nThe dealer has:", dealer_hand)
    print("Total:", total(dealer_hand))
    while True:
        if blackjack == True:
            break
        if total(my_hand) > 21:
            print("Dealer wins!")
            break
        if total(dealer_hand) < 17:
            card = new_card()
            dealer_hand.append(card)
            print("\nDealer is drawing a card . . .")
            time.sleep(2)
            print("\nThe dealer has:", dealer_hand)
            print("Total:", total(dealer_hand))
        if total(dealer_hand) > 21 and blackjack == False:
            print("\nDealer busted -- You WIN!")
            player_won += 1
            player_balance += wager
            break
        elif total(dealer_hand) >= 17 and total(dealer_hand) < 22:
            break

    # Compares dealer and player hands to determine winner
    time.sleep(1)
    if blackjack == True:
        print(f"\n{username} wins!")
        player_balance += wager * 2
    if total(my_hand) > total(dealer_hand) and total(my_hand) <= 21:
        print(f"\n{username} wins!")
        player_won += 1
        player_balance += wager
    if total(my_hand) < total(dealer_hand) and total(dealer_hand) <= 21:
        print("\nDealer wins!")
        player_lost += 1
        player_balance -= wager
    if total(my_hand) == total(dealer_hand):
        print("\nPush.")
    if player_balance == 0:
        print("Sorry, you have no more money and your credit has run out. . . ")
        time.sleep(1)
        print("\nGet outta my casino, you bum!")
        time.sleep(3)
        os.system('cls')
        exit()

    # Logic requesting player input to repeat game or not
    repeat(username)