# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 17:00:42 2016

@author: salwus     VERSION v2
"""
import timeit

a = 2
b = 10
n = 10**5 #ilosc wykonan

def pow_lib(): 
    global a,b   
    return a**b
    
def pow_moja():
	global a,b
	
	
	
	wynik = 1
	while(b):
		if (b & 1):
			wynik *= a
		b>>=1
		a *=a
	return wynik	
	
a = 2
b = 10
n = 10**5 #ilosc wykonan
	
print "a=" ,a 
print "b=",b 
print "n=" ,n
#============ponizsze funkcje zwracaja czas trwania moich funkcji=======
print "time pow_lib = " , timeit.timeit( pow_lib, number=n )
print "time pow_moja = ",  timeit.timeit( pow_moja, number=n )

a = 2
b = 100
n = 10**5 #ilosc wykonan

print "\na=" ,a 
print "b=",b 
print "n=" ,n

print "time pow_lib = " , timeit.timeit( pow_lib, number=n )
print "time pow_moja = ",  timeit.timeit( pow_moja, number=n )

a = 2
b = 1000
n = 10**5 #ilosc wykonan

print "\na=" ,a 
print "b=",b 
print "n=" ,n

print "time pow_lib = " , timeit.timeit( pow_lib, number=n )
print "time pow_moja = ",  timeit.timeit( pow_moja, number=n )
	
a = 2
b = 10000
n = 10**5 #ilosc wykonan

print "\na=" ,a 
print "b=",b 
print "n=" ,n

print "time pow_lib = " , timeit.timeit( pow_lib, number=n )
print "time pow_moja = ",  timeit.timeit( pow_moja, number=n )
if(pow_lib() == pow_moja()):
	print 'wszystko sie zgadza\n\n'

print timeit.timeit('3**2', number=n) , '<-czas 3**2'
print timeit.timeit('3*3', number=n) , '<-czas 3*3\n'

print timeit.timeit('3**4', number=n) , '<-czas 3**4'
print timeit.timeit('3*3*3*3', number=n) , '<-czas 3*3*3*3\n'

print timeit.timeit('3**8', number=n) , '<-czas 3**8'
print timeit.timeit('3*3*3*3*3*3*3*3', number=n) , '<-czas 3*3*3*3*3*3*3*3\n'

print timeit.timeit('3**16', number=n) , '<-czas 3**16'
print timeit.timeit('3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3', number=n) , '<-czas 3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3\n'






