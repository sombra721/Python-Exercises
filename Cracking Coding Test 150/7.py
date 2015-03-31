# -*- coding: utf-8 -*-
"""
Created on Wed Mar 05 20:37:08 2014

@author: Michael
"""

#Write an algorithm such that if an element in an MxN matrixis 0, its entire row
"""
import copy
def set0forMatrix(NxM):
    outputNxM = copy.deepcopy(NxM)
    length = len(NxM)
    width = len(NxM[0])
    print length, width
    for i in range(length):
        for j in range(width):
            if NxM[i][j] == 0:
                print "在", i, j
                for k in range(width):
                    outputNxM[i][k] = 0
                for l in range(length):
                    outputNxM[l][j] = 0
    return outputNxM

N = [[1,0,3], [4,5,6]]
print set0forMatrix(N)
print N
"""

def set0forMatrix(NxM):
    zeros = []
    length = len(NxM)
    width = len(NxM[0])
    for i in range(length):
        for j in range(width):
            if NxM[i][j] == 0:
                zeros.append([i,j])
    if not zeros:
        return NxM
    else:
        for i in xrange(len(zeros)):
            for j in xrange(width):
                NxM[zeros[i][0]][j] = 0
            for k in xrange(length):
                NxM[k][zeros[i][1]] = 0
    return NxM
             
N = [[1,2,0], [4,5,6]]
print set0forMatrix(N)    
