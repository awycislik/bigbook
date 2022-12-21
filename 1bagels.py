"""Bagels, by Al Sweigart al@inventwithpython.com
A deductive logic game where you must guess a number based on clues.
View this code at https://nostarch.com/big-book-small-python-projects
A version of this game is featured in the book "Invent Your Own
Computer Games with Python https://nostrach.com/inventwithpython
Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3  # (!) Try setting this to 1 or 10
MAX_GUESSES = 10


def main():
    print('''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com

    I am thinking about of a {}-digit number with no repeated digits.
    Try to guess that it is. Here are some clues:
    When I say:     That means:
      Pico          One digit is correct but in the wrong position.
      Fermi         One digit is correct and in the right position.
      Bagels        No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:  # Main game loop.
        #This stores the sectet number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))