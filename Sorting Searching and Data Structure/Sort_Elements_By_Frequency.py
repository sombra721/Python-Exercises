# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 00:12:05 2014

@author: Michael
"""
import collections

a = [1,2,3,4,5,1,1,1,6,2,3,3,3,3,3,6,7,3,3,3,2,2,4,6]

a.sort()
temp = collections.Counter(a)

print temp

print temp.keys()
print temp.values()
result = []
#for i in temp.keys():
#    for j in range(len(temp.values())):
#        result.append(i)
#print result