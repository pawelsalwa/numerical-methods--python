# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 21:37:30 2017

@author: salwus
"""

def bisection():
	a,b,c,d,e,f=-5.,-4.,0.,1.,8.,9.
	print bis(a,b)
	print bis(c,d)
	print bis(e,f)
	

def bis(a,b):
	fb=-1. + 39.*b + 4.*b*b - (b**3)

	while(True):
		x=(a+b)/2
		fx=-1. + 39.*x + 4.*x*x - x**3
		
		if(fx==0):
			break
		elif(fx*fb<0):
			a=x
		else:
			fb=fx
			b=x
		if(abs(fx) <= 0.00000001):#dokladnosc
			break
	return x