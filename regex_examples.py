#! /usr/bin/env python3

###################################################################
# sys.argv is a list that contains all command line flags         #
###################################################################
import sys
import pprint
import pyperclip
import re

commaSpacedInt = re.compile(r'^\d{1,3}(,\d{3})*$')
# Numbers
print("Decimal numbers that were found are: ")
mo = commaSpacedInt.search('23,543') 
print(mo.group())
mo = commaSpacedInt.search('1,000,000') 
print(mo.group())
mo = commaSpacedInt.search('32,379') 
print(mo.group())
mo = commaSpacedInt.search('2315') 
if (mo!=None):
    print(mo.group())
mo = commaSpacedInt.search('777') 
if (mo!=None):
    print(mo.group())
mo = commaSpacedInt.search('7.77') 
if (mo!=None):
    print(mo.group())

# Nakamoto
print("")
print("Individuals with the surname Nakamoto that were found are: ")
nakamotoFullname = re.compile(r'[A-Z][A-Za-z]*\s+Nakamoto')
mo = nakamotoFullname.search('Satoshi Nakamoto') 
print(mo.group())
mo = nakamotoFullname.search('RoboCop Nakamoto') 
print(mo.group())
mo = nakamotoFullname.search('Mr. Nakamoto') 
if (mo!=None):
    print(mo.group())
mo = nakamotoFullname.search('Nakamoto') 
if (mo!=None):
    print(mo.group())
