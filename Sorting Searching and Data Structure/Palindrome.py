# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 22:55:10 2014

@author: Michael
"""

a = "55678"
print a[::-1]

if a == a[::-1]:
    print "is Palindrome"
else: 
    print "not Palindrome"