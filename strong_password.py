#! /usr/bin/env python3

#####################################################################
# strong_password.py - uses regular expressions to make sure the    #
#                      password string it is passed is strong.      #
#                      A strong password is defined as one that is: #
#                         * is at least eight characters long       #
#                         * contains both uppercase and lowercase   #
#                         * has at least one digit                  #
#####################################################################
# sys.argv is a list that contains all command line flags           #
#####################################################################
import sys
import pprint
import pyperclip
import re

#    ####################### Regex usage examples ########################
#    # Decimal numbers
#    commaSpacedInt = re.compile(r'^\d{1,3}(,\d{3})*$')
#    print("Decimal numbers that were found are: ")
#    mo = commaSpacedInt.search('2315') 
#    if (mo!=None):
#        print(mo.group())
#    
#    print("")
#    
#    # Nakamoto
#    nakamotoFullname = re.compile(r'[A-Z][A-Za-z]*\s+Nakamoto')
#    print("Individuals with the surname Nakamoto that were found are: ")
#    mo = nakamotoFullname.search('Satoshi Nakamoto') 
#    print(mo.group())
#    mo = nakamotoFullname.search('Mr. Nakamoto') 
#    if (mo!=None):
#        print(mo.group())
#    ####################### Regex usage examples ########################

# check if it's at least 8 chars long
def has_eight_char_n_more(pswd):
    eightChars = re.compile(r'^.{8,}$')
    mo         = eightChars.search(pswd)
    if (mo == None):
        return False
    else:
        return True

# check if it has at lower/uppercase chars
def has_lower_n_upper_case(pswd):
    lowerCase = re.compile(r'[a-z]')
    mo_lc     = lowerCase.search(pswd)
    upperCase = re.compile(r'[A-Z]')
    mo_uc     = upperCase.search(pswd)
    if (mo_lc == None or mo_uc == None):
        return False
    else:
        return True

# check if it has at least 1 digit
def has_one_digit_n_more(pswd):
    digit = re.compile(r'\d')
    mo    = digit.search(pswd)
    if (mo == None):
        return False
    else:
        return True


passwordUnderTest = input()
print("The password under test is: " + passwordUnderTest)
if (has_eight_char_n_more(passwordUnderTest) == False):
    print("The password is less then 8 chars long")
if (has_lower_n_upper_case(passwordUnderTest) == False):
    print("The password doesn't have lower & uppercase chars")
if (has_one_digit_n_more(passwordUnderTest) == False):
    print("The password doesn't have at least 1 digit")
