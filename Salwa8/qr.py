# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 14:58:19 2017

@author: salwus
"""
from math import sqrt
from copy import copy
def qr():
	M = [[1.,2.,3.],
	     [2.,4.,5.],
	     [3.,5.,-1.]]
	Q = [[0.,0.,0.], #nieelastyczne, ale proste
	     [0.,0.,0.],
	     [0.,0.,0.]]
	R = [[0.,0.,0.],
	     [0.,0.,0.],
	     [0.,0.,0.]]
	
	N=len(M)
	
	Lambda=[]
	Prev=[]
	for i in range(0,N):
		Lambda.append(0.)
		Prev.append(1.)
	
	M,Q,R=qrTMP(M,Q,R)
	end = True
	
	while(end):
		end = False
		for i in range(0,N):
			for j in range(0,N):
				M[i][j] = 0
				for k in range(0,N):
					M[i][j] += R[i][k]*Q[k][j]
					
		for i in range(0,N):
			Lambda[i] = M[i][i]
			
		for i in range(0,N):
			if(abs(Prev[i] - Lambda[i]) > 0.00000001):
				end = True
			
		for i in range(0,N):
			Prev[i] = Lambda[i]
		M,Q,R=qrTMP(M,Q,R)
		
	for i in range(0,N):
		print 'L[' + repr(i) + '] = ' + repr(Lambda[i])	
			
			
			
			
			
			
			
			
			
	
#======================================================
def qrTMP(M,Q,R):
	N=len(M)
	a=[]
	M_vec=[]
	
	for i in range(0,N):
		a.append(M[i][0])
		M_vec.append(0.)
	for i in range(0,N):#jendostkowa
		for j in range(0,N):
			if(j==i):
				Q[i][j]=1.
			else:
				Q[i][j]=0.
#=========================	 
	for ite in range(0,N-1):
		norm =0
		for i in range(ite,N):
			norm += a[i]*a[i]
		norm = sqrt(norm)	
		a[ite] -= norm
		norm =0
		for i in range(ite,N):
			norm += a[i]*a[i]
		norm = sqrt(norm)
		for i in range(ite,N):
			a[i] /= norm
		for i in range(0,N):#jendostkowa
			for j in range(0,N):
				if(j==i):
					R[i][j]=1
				else:
					R[i][j]=0
		for i in range(ite,N):
			for j in range(ite,N):
				R[i][j]-= 2*a[i]*a[j]
		for i in range(ite,N):
			a[i] = 0
			for j in range(0,N):
				a[i] += M[j][ite+1]*R[i][j]
		
		for i in range(0,N):
			for j in range(0,N):
				for k in range(0,N):
					if (j==0):
						M_vec[k] = Q[i][k]
					if (k==0):
						Q[i][j] = M_vec[k]*R[k][j]
					else:
						Q[i][j] += M_vec[k]*R[k][j]
#=========================
	
	Q = transp(Q)
	
	for i in range(0,N):
			for j in range(0,N):
				R[i][j] = 0
				for k in range(0,N):
					R[i][j] += Q[i][k]*M[k][j]
	Q = transp(Q)
	return M,Q,R
#======================================================
		   
		   
def transp(X):
	Y = [[0.,0.,0.],
		  [0.,0.,0.],
		  [0.,0.,0.]]
	N = len(X)
	
	for i in range(0,N):
		for j in range(0,N):
			Y[i][j] = X[i][j]

	
	for i in range(0,N):
		for j in range(0,N):
			Y[i][j] = X[j][i]
	return Y


