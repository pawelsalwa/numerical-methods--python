# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 14:01:32 2017

@author: salwus
"""
from potegowa import potegowa

from qr import qr

import timeit

print "wynik potegowej:"
print timeit.timeit( potegowa, number=1 )  ,"<-czas wykonania potegowa()"
print "\nwynik qr:"
print timeit.timeit( qr, number=1 ) ,"<-czas wykonania qr() "  
