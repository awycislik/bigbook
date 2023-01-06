"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/bid-book-small-python-projects
Tags: short, math, simulation"""

import datetime
import random


def get_birthdays(number_of_birthdays):
    """Returns a list of number random date objects for birthdays."""
    arr_birthdays = []
    for num in range(number_of_birthdays):
        # The year is unimportant for our simulation, as long as all
        # arr_birthdays have the same year.
        start_of_year = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        random_numer_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_of_year + random_numer_of_days
        arr_birthdays.append(birthday)
    return arr_birthdays


def get_match(arr_birthdays):
    """Returns the date objects of a birthday that occurs more than once
    in the birthday list."""
    if len(arr_birthdays) == len(set(arr_birthdays)):
        return None  # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(arr_birthdays):
        for b, birthdayB in enumerate(arr_birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday.


# Display the intro:
print('''Birthday Paradox, by Al Sweighart

The Birthday Paradox shows is that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.
''')

# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate (Max 150)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 150):
        numBDays = int(response)
        break  # User has entered a valid amount.
print()

# Generate and display the birthdays:
print('Here are', numBDays, 'birthdays:')
birthdays = get_birthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birtday after the first birtday.
        print(',', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

# Determine if there are two birthdays that match.
match = get_match(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month -1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birtday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print("Let/'s run another 100,000 simulations. ")
simMatch = 0  # How many simulations had matching birthdaus in them.
for i in range(100_000):
    # Report on the progers every 10,000 simulations:
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = get_birthdays(numBDays)
    if get_match(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out if 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a ', probability, '% chance of')
print('having a matching birthday in their group.')
print("That's probably more than you would think!")
