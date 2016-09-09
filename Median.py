# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 17:16:45 2016

@author: Jota Quiroga
"""
import numpy as np



def Median(asd=[]):
    l=len(asd)
    if (len(asd)%2 != 0):
        asd=sorted(asd)
        
        median=asd[int(l/2+0.5)]
        print ("the median is {}".format(median))
        return median
        
    else:
        print ( " No median, pair")
        return -1


lista=[0,3,2,1,6,110,22,33,44,55,66,3]

Median(lista)
