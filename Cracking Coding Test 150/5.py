# -*- coding: utf-8 -*-
"""
Created on Tue Mar 04 23:06:27 2014

@author: Michael
"""

#Implement a method to perform basic string compression using the counts of repeated characters

#aabcccccaa would become a2blc5a3.

#do nothing if this would not make the string smaller.



def stringCompress2(inputString):
    count = 1
    result = []
    i = 0
    while i < len(inputString) - 1:
        if inputString[i] == inputString[i+1]:
            count += 1
            if i+1 == len(inputString)-1:
                count += 1
                result.append(inputString[i])
                result.append(str(count))
        else:
            result.append(inputString[i])
            result.append(str(count))
            count = 1
            if i+1 == len(inputString)-1:
                result.append(inputString[i+1])
                result.append(str(count))
                
        i += 1
    return "".join(result)        
        
            

def stringCompress(inputString):
    output = []
    count = 1
    i = 0
    while i < (len(inputString)-1):
        if inputString[i+1] == inputString[i]:
            count += 1
            if i+1 == len(inputString)-1:
                output.append(inputString[i])
                output.append(str(count))
        else:
            output.append(inputString[i])
            output.append(str(count))
            count = 1
            if i+1 == len(inputString)-1:
                output.append(inputString[i+1])
                output.append(str(count))
        
        i += 1
    return ''.join(output)

a = "aabbcccdddwwwwa"
print stringCompress2(a)
        