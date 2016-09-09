# -*- coding: utf-8 -*-
"""
Created on Wed Sep 07 23:42:41 2016

@author: Jota Quiroga
"""


def Cards(snuke=[], sothe=[]):
    if( len(snuke) == len(sothe)):
        N=len(snuke)
        score=0
        for i in N:
            if(snuke[i] > sothe[i]):
                score=score+1
                print ( " the score was {}".format(score))        
            
                return score 
            
    
    