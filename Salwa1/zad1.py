# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 16:13:58 2016

@author: salwus
"""

import matplotlib.pyplot as plt
from math import *

def D1( f, x, h ):
    return (f(x+h) - f(x)) / h

def D2( f, x, h ):
    return ( f(x+h) - f(x-h) ) / (2.*h)
    
def D4( f, x, h ):
    return ( -f(x+2.*h) + 8.*f(x+h) - 8.*f(x-h) + f(x-2.*h)  ) / (12.* h)


x = 1.
no_h = 60
h = 1.e-6

#print 'D1(sin(1)) = ', D1(sin, x, h)
#print 'D2(sin(1)) = ', D2(sin, x, h)
#print 'D4(sin(1)) = ', D4(sin, x, h)

h_tab = [0.]*no_h
D1_tab = [0.]*no_h
D2_tab = [0.]*no_h
D4_tab = [0.]*no_h

for i in range(no_h):
    if i==0:
        h_tab[i] = 1.
    D1_tab[i] = abs( D1(sin, x, h_tab[i]) - cos(x) )
    D2_tab[i] = abs( D2(sin, x, h_tab[i]) - cos(x) )
    D4_tab[i] = abs( D4(sin, x, h_tab[i]) - cos(x) )
    if i==(no_h-1):
        break
    h_tab[i+1] = h_tab[i]/2.



fig = plt.figure()
plt.loglog(h_tab, D1_tab, label="D1")
plt.loglog(h_tab, D2_tab, label="D2")
plt.loglog(h_tab, D4_tab, label="D4")
plt.title('Salwa zad.1')
plt.xlabel('h')
plt.ylabel("|D-f'|")
plt.legend(bbox_to_anchor=(0.9, 1), loc='upper left', borderaxespad=0.)
fig.savefig('zad1_plot.pdf')
plt.close(fig)



