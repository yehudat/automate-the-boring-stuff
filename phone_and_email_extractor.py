#! /usr/bin/env python3

###################################################################
# phone_and_email_extractor.py - finds all phone numbers and      #
#                                email addresses in the clipboard #
###################################################################
# sys.argv is a list that contains all command line flags       #
#################################################################
import sys
import pprint
import pyperclip
import re

# 1: Create phone number regex.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code - w/ or w/a brackets
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# 2: Create email address regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+    # username
    @                    # @ symbol
    [a-zA-Z0-9.-]+       # domain name
    (\.[a-zA-Z]{2,4})    # dot-something
    )''', re.VERBOSE)

# 3: Find matches in clipboard text.
text = str(pyperclip.paste())
matches = [] # empty tuple

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) #groups[2], groups[4] are hyphens
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text): 
    matches.append(groups[0])

# 4: Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
