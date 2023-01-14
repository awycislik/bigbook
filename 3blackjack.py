"""Blackjack, by Al Sweigart al@inventwithpython.com
2. The classic card game also known as 21. (This version doesn't have
3. splitting or insurance.)
4. More info at: https://en.wikipedia.org/wiki/Blackjack
5. View this code at https://nostarch.com/big-book-small-python-projects
6. Tags: large, game, card game"""

import random, sys

# Set up the constants:
HEARTS = chr(9829)  # Characters 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824)  # Character 9824 is '♠'
CLUBS = chr(9827)  # Character 9827 is '♣'
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'


def main():
    print('''Blackjack, by Al Sweigart
    
    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand to stop taking card.
        On your first play, you can (D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.''')

    money = 5000
    while True: # Main game loop
        # Check if the player has run out of money:
        if money <=0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()

        # Let the player enter their bet for this round:
        print('Money:', money)
        bet = get_bet(money)

        # Give the dealer and player two cards from the deck each:
        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # Handle player actions:
        print('Bet:', bet)
        while True:  # Keep looping until player stands or busts.
            display_hands(player_hand, dealer_hand, False)
            print()

            # Check if the player has bust:
            if get_hand_value(player_hand) > 21:
                break

            # Get
