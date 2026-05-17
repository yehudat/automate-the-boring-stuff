#! /usr/bin/env python3

#################################################################
# table_printer.py - prints list of lists of strings in a table #
#                    Each list becomes a column
#################################################################
# sys.argv is a list that contains all command line flags       #
#################################################################
import sys
import pprint
import pyperclip

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# lol = list of lists
def print_table(lol):
    maxColW = [0]*len(lol) # array of max width of columns, filled with zeros, so far

    for idx in range(len(lol)):
        maxColW[idx] = len(max(lol[idx], key=len)) + 1

    # all lists are of the same length
    for idx in range(len(lol[0])):
        for lolIdx in range(len(lol)):
            myList = lol[lolIdx]
            print(myList[idx].rjust(maxColW[lolIdx]), end="")
        print("")

print_table(tableData)
