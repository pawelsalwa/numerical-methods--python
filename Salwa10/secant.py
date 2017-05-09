# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 00:43:16 2017

@author: salwus
"""

def secant():
	a,b,c,d,e,f=-5.,-4.,0.,1.,8.,9.
	print sec(a,b)
	print sec(c,d)
	print sec(e,f)
	
def sec(a,b):
	fb=-1. + 39.*b + 4.*b*b - (b**3)
	fa=-1. + 39.*a + 4.*a*a - (a**3)

	while(True):
		x=a -fa*(a-b) / (fa-fb)
		fx=-1. + 39.*x + 4.*x*x - x**3
		
		if(fx==0):
			break
		else:
			b=a
			a=x
			fb=fa
			fa=fx
		if(abs(fx) <= 0.00000001):#dokladnosc
			break
	return x
