# -*- coding: utf-8 -*-
"""
Created on Mon Feb 06 00:51:34 2017

@author: salwus
"""

import timeit
from bisection import bisection
from regula import regula
from secant import secant

print "wynik metody rownego podzialu:====================="
print timeit.timeit( bisection, number=1 )  ,"<-czas wykonania bisection()"


print "\n\nwynik metody siecznych:====================="
print timeit.timeit( secant, number=1 )  ,"<-czas wykonania secant()"

				   
print "\n\nwynik regula falsi:====================="
print timeit.timeit( regula, number=1 )  ,"<-czas wykonania regula()"