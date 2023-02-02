"""Caesar Cipher Hacker, by Al Sweigart
This program hacks messages encrupted with the Caesar cipher by doing
a burte force attack against every possible key.
More info at:
https://en,wikipedia.org/wiki/Caesar-cipher#Breaking_the_cipher
View this code at https://nostarch,com/big-bool-small-python-projects
Tags: tiny, beginner, cryptography, math"""

print('Caesar Cipher Hacker, by Al Sweigart')

# Let the user specify the message to hack:
print('Enter the encrypted Caesar cipher message to hack.')
message = input('> ')

# Every possible symbol that can be encrypted/decrypted
# (This must match the SYMBOLS used when encrypting the message.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'

for key in range(len(SYMBOLS)):  # Loop through possible key.
    translated = ''

    # Decrtpt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  # Get the number of the symbol.
            num = num - key  # Decrypt the number.

            # Handle the wrap-around if num is less than 0:
            if num < 0:
                num = num + len(SYMBOLS)

            # Add decrypted number's symbol to translated:
            translated = translated + SYMBOLS[num]
        else:
            # Just add the symbol without decrypting:
            translated = translated + symbol

    # Display the key being tested, along with decrypted text:
    print('Key #{}: {}'.format(key, translated))
