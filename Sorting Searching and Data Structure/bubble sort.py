# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 19:10:06 2014

@author: Michael
"""

def bubblesort(inputList):
    for i in xrange(len(inputList)-2, -1, -1):
        for j in xrange(i, len(inputList)-1):
            if inputList[j] > inputList[j+1]:
                inputList[j], inputList[j+1] = inputList[j+1], inputList[j]
    return inputList
    
a = [11,33,22,55,99,5,3,4,2,1,]

print bubblesort(a)