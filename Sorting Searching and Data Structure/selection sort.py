# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 19:43:53 2014

@author: Michael
"""

def selectionSort(List):
    for i in xrange(len(List)-1, 0, -1):
        Max = 0
        MaxPosition = 0
        for j in xrange(0, i+1):
            if List[j] > Max:
                MaxPosition = j
                Max = List[j]
        List[i], List[MaxPosition] = List[MaxPosition], List[i]
    return List
                
a = [5,4,7,3,8,9,1,10,2]

print selectionSort(a)            
            
    