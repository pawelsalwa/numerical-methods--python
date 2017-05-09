# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 14:43:16 2017

@author: salwus
"""

def pow_lib():    
    return a**b
    
def pow_moja():
    a_loc = a
    i=0
    while i<b-1:
        a_loc *= a
        i += 1
    
    return a_loc
				
				
def pow_moja2():
	wynik = 1
	for i in range(0,b):
		wynik *= a
		
		
	return wynik
def rekI():
	wynik = rek(a,b)
	
	return wynik
	
def rek(a,b):
	
	if (b == 0):
		return 1
	else:
		wynik = a*rek(a,b-1)
		return  wynik