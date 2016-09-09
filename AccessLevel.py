# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 13:30:46 2016

@author: Jota Quiroga
"""

def canAccess(minPermission, Rights=[]):
    
    
    
    largo=len(Rights)    
    
    
    for i in range (largo):
        
        if ( Rights[i]>= minPermission ):
            
            Rights[i]="A"
            
        else:
            
            Rights[i]="D"
            
    
    print ("Access {}".format(Rights))
    return Rights
    
    
    
A=[0,1,2,3,4,5]

canAccess(2,A)

    