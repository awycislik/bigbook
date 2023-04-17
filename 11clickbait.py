"""Clickbait Headline Generator, by Al Sweigart
A clickbait headlline generator for soulless content farm website.
View this code at https://nostarch .com/big-book-small-python-projects
Tags: large, beginner, humor, word"""

import random

# Set up the constants:
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pensylwania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Showel', 'Peleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Dount Shop', 'Apocalypte Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def main():
    print('Clickbait Headline Generator')
    print('By Al Sweigart al@inventwithpython.com')
    print()

    print('Our website needs to trick people into looking at ads!')
    while True:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            number_of_headlines = int(response)
            break

    for i in range(number_of_headlines):
        clickbait_type = random.randint(1, 8)

        if clickbait_type == 1:
            headline = generate_are_millennials_killing_headline()
        elif clickbait_type == 2:
            headline = generate_what_you_dont_know_headline()
        elif clickbait_type == 3:
            headline = generate_big_companies_hate_her_headline()
        elif clickbait_type == 4:
            headline = generate_you_wont_believe_headline()
        elif clickbait_type == 5:
            headline = generate_dont_want_you_to_know_headline()
        elif clickbait_type == 6:
            headline = generate_gift_idea_headline()
        elif clickbait_type == 7:
            headline = generate_reason_why_headline()
        elif clickbait_type == 8:
            headline = generate_job_automat_headline()

        print(headline)
    print()

    website = random.choice(['wobsite', 'blag', 'Facebuuk', 'Gogles',
                            'Facesbook', 'Tweedie', 'Pastgram'])
    when = random.choice(WHEN).lower()
    print('Post these to our', website, when, "or you're fired")


# Each of these functions returns a different type of headlin:
def generate_are_millennials_killing_headline():
    noun = random.choice(NOUNS)
    return 'Are Millennials Killing the {} Industry?'.format(noun)


def generate_what_you_dont_know_headline():
    noun = random.choice(NOUNS)
    plural_noun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {}, {} Could Kill You {}'.format(noun, plural_noun, when)


def generate_big_companies_hate_her_headline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(pronoun, state, noun1, noun2)


def generate_you_wont_believe_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return "You won't believe What This {} {} Found in {} {}".format(state, noun, pronoun, place)


def generate_dont_want_you_to_know_headline():
    plural_noun1 = random.choice(NOUNS) + 's'
    plural_noun2 = random.choice(NOUNS) + 's'
    return "What {} Don't Want You To Know About {}".format(plural_noun1, plural_noun2)


def generate_gift_idea_headline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return "{} Gift Ideas to Give Your {} From {}".format(number, noun, state)


def generate_reason_why_headline():
    number1 = random.randint(3, 19)
    plural_noun = random.choice(NOUNS) + 's'
    # number2 should be no larger than nunber1
    number2 = random.randint(1, number1)
    return "{} Reason Why {} Are More Interesting Than You Think " \
           "(Number {} Will Surprise You!".format(number1, plural_noun, number2)


def generate_job_automat_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return "This {} {} Didn't Think Robots Would Take {} Job. {} Were Wrong".format(state, noun, pronoun1, pronoun2)
    else:
        return "This {} Didn't Think Robots Would Take {} Job. {} Was Wrong".format(state, noun, pronoun1, pronoun2)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
