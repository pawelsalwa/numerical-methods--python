# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 14:56:18 2017

@author: salwus
"""

from math import sqrt

def potegowa():
	M = [[1.,2.,3.],
	     [2.,4.,5.],
	     [3.,5.,-1.]]
	
	N=len(M)
	X=[]
	temp2=[]
	X_prev=[]
	Z=[]
	Lambda = 0.
	Evectors=[[0.,0.,0.],[0.,0.,0.],[.0,0.,0.]]
	Eigenvalue= []
	
	for i in range(0,N):
		X.append(0.)
		temp2.append(0.)	
		X_prev.append(1.)
		Z.append(0.)
		Eigenvalue.append(0.)
#		for j in range(0,N):pass
#			Evectors[i][j].append(0.)
	
	for L in range(0,N):
		while(True):
			for i in range(0,N):
				X[i] =0
				for j in range(0,N):
					X[i] += M[i][j]*X_prev[j]
					
				
			for k in range(0,L): # deflacja
				temp = 0
				for i in range(0,N):
					temp += Evectors[i][k]*X[i]
					temp2[i] = Evectors[i][k]
		  		for i in range(0,N):
					temp2[i] *= temp
		  		for i in range(0,N):
				   X[i] -= temp2[i]
				   
			for i in range(0,N):
			   Z[i]= X[i]

			X_norm = 0
			for i in range(0,N):
				X_norm += X[i]*X[i]
			X_norm = sqrt(X_norm)
			
			for i in range(0,N):
				X[i] /= X_norm
			if ( abs( Lambda - X_norm ) < 0.00000001):
				break
			for i in range(0,N):
				X_prev[i] = X[i]
			Lambda = X_norm
			
		X_norm = 0
		for i in range(0,N):
			X_norm += Z[i]*X_prev[i]
		Eigenvalue[L] = X_norm
			
		for i in range(0,N):
			Evectors[i][L] = X[i]
		for i in range(0,N):
			X_prev[i] = 1
			
			
			
	for i in range(0,N):
		print 'L[' + repr(i) + '] = ' + repr(Eigenvalue[i])