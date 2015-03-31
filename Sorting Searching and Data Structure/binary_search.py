# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 22:37:59 2014

@author: Michael
"""

a = [1,4,6,7,8,9,10,14,16]

def binarySearch(array, key, low, high):  
    if low > high: # termination case  
        return -1  
  
    middle = (low + high) / 2 # gets the middle of the array  
  
    if array[middle] == key:  # if the middle is our key  
        return middle  
    elif key < array[middle]: # our key might be in the left sub-array  
        return binarySearch(array, key, low, middle-1)  
    else:                     # our key might be in the right sub-array  
        return binarySearch(array, key, middle+1, high)  
        
print binarySearch(a, 14, 0, len(a))