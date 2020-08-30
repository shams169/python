#!/usr/bin/env python3

import sys

s1 = input(r"Enter String 1: ")
s2 = input(r"Enter String 2: ")

# Check if the two strings are of equal length
if not len(s1) == len(s2):
    sys.exit("The two strings are not of equal length")


sort_1 = (sorted(s1))
sort_2 = (sorted(s2))

print("Sorted 1: {} and Sorted 2: {}".format(sort_1, sort_2))

if sort_1 == sort_2:
    print("The words {} and {} are anagrams".format(s1, s2))