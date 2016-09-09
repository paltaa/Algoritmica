# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 15:40:52 2016

@author: Jota Quiroga
"""

"""Problem Statement
    	
This problem statement contains superscripts that may not display properly outside the applet.

Kitayuta Mart is the largest supermarket in Shuseki Kingdom, offering a great variety of food and household products.
The main products are fruits, especially apples.
 The price system is a little special: the original price of an apple is K yen (the currency of the kingdom).
 However, if a customer wants to buy more than one apple, the second apple will cost 2*K yen, the third apple will cost 22*K yen, and so on.
 In general, if a customer is buying n apples, the actual price of the i-th (1 <= i <= n) apple will be 
 
 2i-1*K yen.

Lun the dog loves apples. She has just bought some number of apples at Kitayuta Mart.
 The prices of those apples were calculated using the above formula. The total she paid for her apples was T yen.
 You are given two ints: K and T. Find and return the number of the apples that Lun has bought.
 It is guaranteed that K and T are such that the answer exists and is unique.

 
Definition
    	
Class:	KitayutaMart2
Method:	numBought
Parameters:	int, int
Returns:	int
Method signature:	int numBought(int K, int T)
(be sure your method is public)
    
 
Constraints
-	K will be between 80 and 160, inclusive.
-	T will be between 80 and 163,680, inclusive.
-	The input will be such that the answer exists and is unique."""



def Apples(K, T ):
    #K original price, T total price for apples

    numBought=(T/K)**(0.5)
    numBought=round(numBought)
        
    print "the number of apples bought is : {} " .format(numBought)


Apples(100,100)
Apples(100,300)
Apples(150,1050)


                
    