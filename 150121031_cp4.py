import sys
import math
import copy

'''
=============================================
! Lab No: 4
! Title : power
! Date: 27/8/2017
! Name : Parismita Das
! Roll No: 150121031
!Email : parismita@iitg.ernet.in
============================================='''

#####################Input##############################
filename = 'a.txt'
input_filename=open(filename)
with input_filename as f:
    content = f.readlines()
content = [x.strip().split(" ") for x in content]
####################################################

#################___Pivoting____########################
def pivot(A,n):
	for i in range(n):
		temp=i
		if A[i][i]==0:
			for j in range(i+1,n):
				if A[j][i]!=0:
					A[i],A[j]=A[j],A[i]
					break		
			
	return A
				

#################___Get_LU___#########################
def getLU(A,n):
	L=[[0.0 for i in range(n)]for j in range(n)]
	for i in range(n-1):
		for j in range(i+1,n):
			if A[j][i]!=0:			
				c=float(A[j][i]/A[i][i])
				for p in range(n):
					A[j][p]=A[j][p]-A[i][p]*c
				L[j][i]=c
	for i in range(n):
		L[i][i]=1
	return L,A


#################___Forward_sub___######################
def fore(L,B,n):
	Y=[0 for i in range(n)]
	Y[0]=B[0]
	for i in range(n):
		temp=B[i]
		for j in range(i):
			temp=temp-L[i][j]*Y[j]
		Y[i]=temp/L[i][i]
	return Y

#################___Backward_sub___######################
def back(U,Y,n):
    
	X=[0 for i in range(n)]
	if U[n-1][n-1]!=0:
	    X[n-1]=Y[n-1]/U[n-1][n-1]	
	for i in range(n-2,-1,-1):	
		temp=Y[i]	
		for j in range(i+1,n):
			temp=temp-U[i][j]*X[j]	
		if U[i][i]!=0:
		    X[i]=temp/U[i][i]	

	return X


######################__power__#############################
def power(A,m,z):

	C = copy.deepcopy(A)
	A=pivot(A,m)
	L,U=getLU(A,m)
	A = copy.deepcopy(C)

	'''print "=========================="
	print "Matrix L"
	print "=========================="
	for i in range(m):
		print L[i]

	print "=========================="
	print "Matrix U"
	print "=========================="
	for i in range(m):
		print U[i]'''

	D = Ain(A,L,U,m) 

	n=m
	itt = 100

	#--------------------------------------------------------------------------------------------------
	x=[5.0 for i in range(n)]
	i=1
	k=0
	lamdama = -1
	while(i):
		y=[0.0 for p in range(n)]
		for j in range(n):
			for k in range(n):
				y[j]=y[j]+C[j][k]*x[k]
		x=y
		ma=x[0]
		for j in range(n):
			if abs(ma)<abs(x[j]):
				ma=x[j]
				
		for k in range(n):
			x[k]=x[k]/ma

		y=[0.0 for i in range(n)]
		for i in range(n):
			for j in range(n):
				y[i]=y[i]+C[i][j]*x[j]
		if(x[0]==0.0):
			continue
		k = lamdama
		lamdama=y[0]/x[0] #check if zeroth entry is non zero
		print "X: \n",x	
		print "max lambda: ",lamdama
		if(abs(abs(k)-abs(lamdama))<z):
			i = 0
			break

#---------------------------------------------------------------------------------------------------------------------
	x=[2.0 for i in range(n)]
	i=1
	k=0
	lamdami = -1
	while(i):
		y=[0.0 for p in range(n)]
		for j in range(n):
			for k in range(n):
				y[j]=y[j]+D[j][k]*x[k]
		x=y
		ma=x[0]
		for j in range(n):
			if abs(ma)<abs(x[j]):
				ma=x[j]
		for k in range(n):
			x[k]=x[k]/ma
		
		y=[0.0 for i in range(n)]	

		for i in range(n):
			for j in range(n):
				 y[i]=y[i]+D[i][j]*x[j]
		k = lamdami
		lamdami=y[0]/x[0] #check if zeroth entry is non zero
		lamdami=1/lamdami

		print "X: \n",x
		print "min lambda: ",lamdami
		if(abs(abs(k)-abs(lamdami))<z):
			i = 0
			break

	#---------------------------------------------------------------------------------------------------------------
	print "\nThe values you have been calculated "
	print "Max:  ",round(abs(lamdama),6)
	print "Min:  ",round(abs(lamdami),6) 
	return round(abs(lamdama),6), round(abs(lamdami),6)      
##################A inverse################################
def Ain(A,L,U,m):
	Ai=[]
	B = [[0 for i in range(m)]for j in range(m)]
	for i in xrange(m):
		B[i][i]=1
	X = []
	for i in xrange(m):
		Y=fore(L,B[i],m)
		X=back(U,Y,m)
		Ai.append(X)
	Ai = zip(*Ai)
	'''print "=========================="
	print "Matrix A(inverse)"
	print "=========================="
	for i in range(m):
		print Ai[i]

	I = [[sum(a*b for a,b in zip(A_row,Ai_col)) for Ai_col in zip(*Ai)] for A_row in A]
	print "=========================="
	print "Matrix A*A(inverse) is identity"
	print "=========================="
	for i in range(m):
		print I[i]'''
	return Ai
				
#####################___Main__Prog__##########################

print "\nPlease enter the tolerance you require"
y=int(raw_input().strip())
z=1.0000000000000
for i in range(y):
	z=z/10
m = int(content[0][0])
#x = int(content[0][0])
A = [[0 for i in range(m)] for j in range(m)]
for i in xrange(1,m+1):
	A[i-1] = map(float,content[i])
a,b=power(A,m,z)
m1 = int(content[m+1][0])
A = [[0 for i in range(m1)] for j in range(m1)]
k = 0
for i in xrange(m+2,m+m1+2):
	A[k] = map(float,content[i])
	k+=1
c,d=power(A,m1,z)

#-----------------------------------------------------
print"\n\n################################"
print "Problem 1:"
print "max eigenvalue:",a
print "min eigenvalue:",b
print"################################"
print "Problem 2:"
print "max eigenvalue:",c
print "min eigenvalue:",d