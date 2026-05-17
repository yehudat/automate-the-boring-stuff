#! /usr/bin/env python3

#######################################################################################################
# strip_implemented_by_regex.py - returns a copy of the string, in which all chars have been stripped #
#                                 from the beginning and the end of the string (default whitespace    #
#                                 characters).                                                        #
# Example:                                                                                            #
#     str = "0000000This is string example....wow!!!0000000";                                         #
#     print str.strip( '0' )                                                                          #
#                                                                                                     #
#     Returns:                                                                                        #
#         This is string example....wow!!!                                                            #
#######################################################################################################
# sys.argv is a list that contains all command line flags                                             #
#######################################################################################################
import sys
import pprint
import pyperclip
import re

string = input()

char = input()

#What if on char input() the user pressed ENTER?
if (char == ""):
    char = " "
    print("Striping whitespaces")
else:
    print("Striping " + char)

charToStripInBeginning = re.compile(r'^(%s)*'%char)
charToStripInEnd       = re.compile(r'(%s)*$'%char)

stringStrippedFromBeginning = charToStripInBeginning.sub('', string)
stringStrippedFromEndToo    = charToStripInEnd.sub('', stringStrippedFromBeginning)

print("The stripped string is: " + stringStrippedFromEndToo)
