#! /usr/bin/env python3

#############################################################
# count_ones.py - count one in an integer, by using         #
#                 bit-wise operators                        #
#############################################################
import pprint

vector = int(input(), 2)
print("The vector of bits is: " + bin(vector))

count = 0
while (vector != 0):
    pprint.pprint(str(vector) + "%2=" + str(vector%2))
    count += vector % 2
    vector = vector >> 1

print("The vector of bits has " + str(count) + " ones")
