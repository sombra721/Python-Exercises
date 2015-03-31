# -*- coding: utf-8 -*-
"""
Created on Tue Mar 04 23:32:52 2014

@author: Michael
"""

# Rotate a NxN matrix 90 degrees
# 一直有遇到卡住的地方, 若newN沒用成np中的array type, 在寫入新值時會將每一個都覆蓋

import numpy as np

def matrixrot90(N):
    length = len(N[0]) 
    newN = [[0]*length]*length
    newN = np.asarray(newN)
    print newN[0][0]
    for i in range(length):
        for j in range(length):
            newN[i][j] = N[length-1-j][i]
    print newN  
        
originN = [[1,2,3],[4,5,6],[7,8,9]]
matrixrot90(originN)

#a = [[0]*3]*3
#print a[2]