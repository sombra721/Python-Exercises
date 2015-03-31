# -*- coding: utf-8 -*-
"""
Created on Tue Mar 04 20:56:59 2014

@author: Michael
"""
#using a list to store each char and change space to '%20', then join list into a string

def replaceSpace(string):
    string = list(string)
    print string
    for i in range(len(string)):
        if string[i] == ' ':
            string[i] = '%20'
    return "".join(string)


print replaceSpace(" dwd ww d")