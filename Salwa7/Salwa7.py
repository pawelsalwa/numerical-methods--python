# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 20:34:45 2017

@author: salwus
"""
#===================================================================
def relaksacyjna(M, b, gamma):
	N=len(M)
	D=[]
	X=[]

	for i in range(0,N):
		X.append(1.)
		D.append(1.)
	
	iterator=0

	end=False

	while(not end):
		end=True
		iterator +=1
								
		for i in range(0,N):
			X[i] = b[i]
			for j in range(0,N):
				X[i] -= M[i][j]*D[j]

			X[i] = D[i] + (gamma*X[i])		

		for i in range(0,N):
			if( abs(D[i] - X[i]) > 0.000000001):
				end=False # tutaj sprawdza czy dokladnosc wyniku jest wystarczajaca
			D[i] = X[i]
			
	for i in range(0,N):
		print 'X[' + repr(i) + '] = ' + repr(X[i])
#======================================================
def jacobiego(M,b):

	T = [[ 0., 0., 0.],
		[ 0., 0., 0.],
	     [ 0., 0., 0.]]
	
	D=[]
	C=[]
	X=[]

	N=len(M)	

	for i in range(0,N):
		D.append(0.)
		C.append(0.)
		X.append(0.)

	for i in range(0,N):
		D[i] = 1/M[i][i]
		C[i] = D[i]*b[i]
		D[i] *= -1
		
		
	for i in range(0,N):
		for j in range(0,N):
			if(j != i):
				T[i][j] = M[i][j] * D[i]
		D[i]=0.

	end = False
	
	while(not end):
		end = True
		
		for i in range(0,N):
			X[i] = C[i]
			for j in range(0,N):
				if(j != i):
					X[i] += T[i][j]*D[j]
		for i in range(0,N):
			if ( abs(D[i] - X[i]) > 0.000000001):
				end = False
			D[i]=X[i]
				
	for i in range(0,N):
		print 'X[' + repr(i) + '] = ' + repr(X[i])			
#======================================================	
def gaussSeidel(M,b):
	
	T = [[ 0., 0., 0.],
		[ 0., 0., 0.],
	     [ 0., 0., 0.]]
	
	D=[]
	C=[]
	X=[]

	N=len(M)	

	for i in range(0,N):
		D.append(0.)
		C.append(0.)
		X.append(0.)

	for i in range(0,N):	
		D[i] = 1/M[i][i]
		C[i] = D[i]*b[i]
		D[i] *= (-1)

	for i in range(0,N):
		for j in range(0,N):
			if(j != i):
				T[i][j] = M[i][j]*D[i]
		D[i] = 0
	
	end=False
        
	while(not end):
		end = True
		
		for i in range(0,N):
			X[i] = C[i]
			for j in range(0,N):
				if(j != i):
					if(i > j):
						X[i] += T[i][j]*X[j]																
					elif(i < j):
						X[i] += T[i][j]*D[j]

		for i in range(0,N):
			if ( abs(D[i] - X[i]) > 0.000000001):
				end = False
			D[i]=X[i]
				
	for i in range(0,N):
		print 'X[' + repr(i) + '] = ' + repr(X[i])
#======================================================
def sor(M,b,omega):
	
	D=[]
	X=[]

	N=len(M)	

	for i in range(0,N):
		D.append(0.)
		X.append(0.)
	
	end=False
        
	while(not end):
		end = True
		
		for i in range(0,N):
			X[i] = b[i]
			for j in range(0,N):
				if(j != i):
					if(i > j):
						X[i] -= M[i][j]*X[j]																
					elif(i < j):
						X[i] -= M[i][j]*D[j]
			X[i] =(1-omega)*D[i]+omega/M[i][i]*X[i]

		for i in range(0,N):
			if ( abs(D[i] - X[i]) > 0.000000001):
				end = False
			D[i]=X[i]
				
	for i in range(0,N):
		print 'X[' + repr(i) + '] = ' + repr(X[i])
#======================================================
	
	
print 'start'

A = [[ 4.,-1., 0.],
	[-1., 4.,-1.],
	[ 0.,-1., 4.]]
	
B = [2.,
	6.,
	2.]

import timeit
#duplikuje mi tutaj output- nie wiem czemu-dlatego usunalem zduplikowana czesc w opisie dla przejzystosci
t = timeit.Timer(stmt="Salwa7.relaksacyjna(Salwa7.A, Salwa7.B,0.25)", setup="import Salwa7")  
print "czas relaksacyjnej: " + repr(t.timeit(1))+ '\n\n'
del t
t = timeit.Timer(stmt="Salwa7.jacobiego(Salwa7.A, Salwa7.B)", setup="import Salwa7")  
print "czas jacobiego: " + repr(t.timeit(1)) + '\n\n'
del t
t = timeit.Timer(stmt="Salwa7.gaussSeidel(Salwa7.A, Salwa7.B)", setup="import Salwa7")  
print "czas gausSeidel: " + repr(t.timeit(1))+ '\n\n'
del t
t = timeit.Timer(stmt="Salwa7.sor(Salwa7.A, Salwa7.B, 1.25)", setup="import Salwa7")  
print "czas succ OverRelaxation: " + repr(t.timeit(1))+ '\n\n'
del t
print 'koniec'
#print 'relaksacyjna:'
#relaksacyjna(A,B, 0.25)
#print 'jacobi:'
#jacobiego(A,B)
#print 'gausSeidel:'
#gaussSeidel(A,B)
#print 'succ OverRelaxation:'
#sor(A,B,1.25)


























