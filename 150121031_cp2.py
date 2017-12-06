import sys
import math
import copy

'''
=============================================
! Lab No: 2
! Title : LU
! Date: 17/8/2017
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




#################___Printer____######################
def prin(A,B,n):
	print "=========================="
	print "Matrix A and vector B"
	print "=========================="
	for i in range(n):
		print A[i]," ----> ",B[i] 
	print "=========================="

def pr(X,n):

	print "Solutions:"
	for i in xrange(n):
		print "X",i,": ",X[i]

#################___Pivoting____########################
def pivot(A,B,n,i):
	mi = i
	for x in xrange(i+1,n):
		if(A[x][i]>A[mi][i]):
			mi = x

	A[i],A[mi] = A[mi],A[i]
	B[i],B[mi] = B[mi],B[i]
	return A,B
				

#################___Get_L___#########################
def getLU(A,B,n):
	L=[[0.0 for i in range(n)]for j in range(n)]
	for i in range(n-1):
		A,B=pivot(A,B,n,i)
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


######################__DO_little__#############################
def dolittle(A,B,m):
	#print "\nPlease enter solution matrix"

	C = copy.deepcopy(A)
	#B=map(float, raw_input().strip().split())
	prin(A,B,m)
	
	L,U=getLU(A,B,m)
	A = copy.deepcopy(C)
	Y=fore(L,B,m)
	X=back(U,Y,m)

	print "=========================="
	print "Matrix L"
	print "=========================="
	for i in range(m):
		print L[i]

	print "=========================="
	print "Matrix U"
	print "=========================="
	for i in range(m):
		print U[i]


	print "\nThe loong wait has completed\n"
	q=-1
	for i in range(m):
		if U[i][i]==0:
			q=0
	if q==0:
		print "Sorry no solution\n"
	else:
		pr(X,m)  

	Ain(A,L,U,m) 
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
	print "=========================="
	print "Matrix A(inverse)"
	print "=========================="
	for i in range(m):
		print Ai[i]

	I = [[sum(a*b for a,b in zip(A_row,Ai_col)) for Ai_col in zip(*Ai)] for A_row in A]
	print "=========================="
	print "Matrix A*A(inverse) is identity"
	print "=========================="
	for i in range(m):
		print I[i]
	

		
####################___Cheloski___########################		
def chelk(A,m):
	L=[[0 for i in range(m)]for j in range(m)]
	LT=[[0 for i in range(m)]for j in range(m)]
	L[0][0]= math.sqrt(A[0][0])
	
	#Doing for off diagonal elements and diagonal sepertely using if else
	
	for i in range(1,m):
		for j in range(i+1):
			temp=A[i][j]
			if (i==j) :
				for k in range(i):
					temp=temp-(L[i][k]*L[i][k])
				L[i][i]= math.sqrt(temp)	
			elif (i!=j):
				for k in range(j):
					temp=temp-L[i][k]*L[j][k]
				L[i][j]=temp/L[j][j]
	
	for i in range(m):
		for j in range(m):
			LT[i][j]=L[j][i]
			
	#X=back(LT,B,m)		
	print "=========================="
	print "Matrix L "
	print "=========================="
	for i in range(m):
		print L[i]
	print "\n=========================="
	print "Matrix L(transpose) "
	print "=========================="
	for i in range(m):
		print LT[i]

	#mat-mul to get A
	A_updated = [[sum(a*b for a,b in zip(L_row,LT_col)) for LT_col in zip(*LT)] for L_row in L]

	print "\n=========================="
	print "Matrix updated A "
	print "=========================="
	for i in range(m):
		print A_updated[i]

	print "\n=========================="
	print "Matrix A "
	print "=========================="
	for i in range(m):
		print A[i]
	#Now we need to do forward substitution
	'''Sol=fore(L,X,m)
	print "\n\nLong wait is over \n"
	print "The solution is\n"
	pr(Sol,m)'''
				
#####################___Main__Prog__##########################
'''
print "Please enter dimensions of the matrix"
m=int(raw_input().strip())
A=[]
print "\nPlease enter matrix"
for i in range(m):
	a=map(float, raw_input().strip().split())
	A.append(a)


print "\nPlease choose method"
print "Enter 1 for dolittle and 2 for chowelski\n"
x=int(raw_input().strip())
if x==1:
	dolittle(A,m)
if x==2:
	chelk(A,m)'''



m = int(content[1][0])
#x = int(content[0][0])
A = [[0 for i in range(m)] for j in range(m)]
for i in xrange(2,m+2):
	A[i-2] = map(float,content[i])
B = map(float,content[m+2])
dolittle(A,B,m)
m1 = int(content[m+3][0])
A = [[0 for i in range(m1)] for j in range(m1)]
k = 0
for i in xrange(m+4,m+m1+4):
	A[k] = map(float,content[i])
	k+=1
chelk(A,m1)

