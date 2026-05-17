#! /usr/bin/env python3

#############################################################
# bullet_point_adder.py - bullet adder for Wiki             #
#############################################################
# sys.argv is a list that contains all command line flags   #
#############################################################
import sys
import pprint
import pyperclip

# 1. Paste text from the clipboard
txt = pyperclip.paste()

# 2. Add '* ' before each and every bullet separated by '\n'
txtLines = txt.split('\n')
for i in range(len(txtLines)):    # loop through all indexes in the "txtLines" list
    txtLines[i] = '* ' + txtLines[i] # add star to each string in "txtLines" list

modifiedTxt = '\n'.join(txtLines)

# 3. Copy the new text to the clipboard
pyperclip.copy(modifiedTxt)

# 4. Print the text for debug
print(modifiedTxt)
