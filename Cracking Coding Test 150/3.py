# -*- coding: utf-8 -*-
"""
Created on Tue Mar 04 20:33:09 2014

@author: Michael
"""

# Given two strings, write a method to decide if one is a permutation of the other.
# A smart way is to sort two strings then compare them

def determinePermutation(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        return sorted(string1) == sorted (string2)

a = "bdwsa"
b = "sabdw"

print determinePermutation(a,b)
