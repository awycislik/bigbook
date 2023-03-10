# """Calendar Maker, by Al Sweigart
# Crate monthly calendars, saved to a text file and fit for printing.
# View this code at https://nostarch.com.big-book-small-python-projects
# Tags: short"""
#
# import datetime
#
# # Set up the constants:
# DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
#         'Saturday', 'Sunday')
# MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
#           'August', 'September', 'October', 'November', 'December')
#
# print('Calendar Maker, by Al Sweigart ')
#
# while True:  # Loop to get a year from the user.
#         print('Enter the year for the calendar:')
#         response = input('> ')
#
#         if response.isdecimal() and int(response) > 0:
#                 year = int(response)
#                 break
#
#         print('Please enter a numeric year, like 2023.')
#         continue
#
# while True:  # Loop to get a month from the user.
#         print('Enter the month for the calendar, 1-12')
#         response = input('> ')
#
#         if not response.isdecimal():
#                 print('Please enter a numeric month, like 3 for March.')
#                 continue
#
#         month = int(response)
#         if 1 <= month <= 12:
#                 break
#
#         print('Please enter a number from 1 to 12.')
#
#
# def get_calendar_for(year, month):
#         cal_text = ''  # cal_text will contain the string of our calendar
#
#         # Put the month and year at the top of the calendar:
#         cal_text += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
#
#         # Add the days of the week labels to the calendar:
#         # (!) Try changing this to abbreviations: SUN, MON, TUE, etc.
#         cal_text += '...Monday...Tuesday...Wednesday...Thursday...Friday...Saturday...Sunday..\n'
#
#         # The horizontal line string that separate weeks:
#         week_separator = ('+----------' * 7) + '|\n'
#
#         # The blank rows have ten spaces in between the | day separators:
#         blank_row = ('|         ' * 7) + '|\n'
#
#         # Get the first date in the month. (The datetime module handles all
#         # the complicated calendar stuff for us here.)
#         current_date = datetime.date(year, month, 1)
#
#         # Roll back current_date until it is Sunday. (weekday() returns 6
#         # for Sunday, not 0.)
#         while current_date.weekday() != 6:
#                 current_date -= datetime.timedelta(days=1)
