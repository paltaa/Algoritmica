# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 12:42:52 2016

@author: Jota Quiroga
"""

def GetDay(notDays=[]):
    Days= ["Mon", "Tue", "Wed", "Thu", "Fri","Sat", "Sun"]
   
    largo=len(notDays)
    
    if (largo ==  6 ):
        
        for i in range(largo):
            
            for j in range(largo):
                
                if(Days[i]==notDays[j]):
                    
                    Days[i]=0
                    
       # print(" Your meeting is :{}".format(Days))           
        
        
        for k in range(len(Days)):
            
            if (Days[k]!=0):
                
                print(" Your meeting is :{}".format(Days[k]))           
                
                
                return Days[k]
                

Days= ["Mon", "Wed","Thu", "Fri","Sat","Sun"]


GetDay(Days)        