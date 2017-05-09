# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 00:12:31 2017

@author: salwus
"""

def regula():
	a,b,c,d,e,f=-5.,-4.,0.,1.,8.,9.
	print reg(a,b)
	print reg(c,d)
	print reg(e,f)
	
def reg(a,b):
	fb=-1. + 39.*b + 4.*b*b - (b**3)
	fa=-1. + 39.*a + 4.*a*a - (a**3)

	while(True):
		x= (fb*a-fa*b)/(fb-fa)
		fx=-1. + 39.*x + 4.*x*x - x**3
		
		if(fx==0):
			break
		elif(fx*fa<0):
			b=x
			fb=fx
		else:
			a=x
			fa=fx
		if(abs(fx) <= 0.00000001):#dokladnosc
			break
	return x

