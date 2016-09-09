# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 16:08:20 2016

@author: Jota Quiroga
"""

def findAnnoyance(String, asno=[]):
    N=len(asno)
    
    Total=0
    for i in range(1, N): 
        if(String[i] == "b" ):
            for j in range(i):
                Total = Total + asno[j]
    
    print "The total Annoyance is : {}".format(Total) 
    return Total
            
wea="bbbbb"
d=[1,1,1,1,1]

findAnnoyance(wea,d)

weks="bbeebeebeeeebbb"
flos=[58,517,301,524,79,375,641,152,810,778,222,342,911,313,336]
findAnnoyance(weks,flos)