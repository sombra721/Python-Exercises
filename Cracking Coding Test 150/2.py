# -*- coding: utf-8 -*-
"""
Created on Tue Mar 04 20:14:48 2014

@author: Michael
"""

# Implement a function that reverses a string
# String cannot be modified in Python, so needed to convert the string to list
a = "abcdefghijk"

print a[5]

def stringReverse(inputString):       
    stringList = list(inputString)
    b = len(stringList)
    for i in range(b/2):
        stringList[i], stringList[b-1-i] = stringList[b-1-i], stringList[i]
    inputString = ("").join(stringList)
    print stringList
print stringReverse(a)
    
    