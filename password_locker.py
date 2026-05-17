#! /usr/bin/env python3

#############################################################
# password_locker.py - An insecure password locker program. #
#############################################################
# sys.argv is a list that contains all command line flags   #
#############################################################
import sys
import pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

#Command line parsing. Length of 2 means 1 argument, as the 
#first argument is the program itself
if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]    # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
