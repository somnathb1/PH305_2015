import sys


'''=============================================
! Lab No: 1
! Title : Matrix Computation
! Date: 08/08/2017
! Name : Parismita Das
! Roll No: 150121031
!Email : parismita@iitg.ernet.in
============================================='''



def pivot(A,i,n,B):
	mi = i
	for x in xrange(i+1,n):
		if(A[x][i]>A[mi][i]):
			mi = x

	A[i],A[mi] = A[mi],A[i]
	B[i],B[mi] = B[mi],B[i]
	return A,B

def pr(A,B,X):
	print "Matrix A and vector be after elimination"
	print "========================================"
	print "A:"
	for i in xrange(n):
		print A[i]
	print "B:"
	print B
	print "Solutions:"
	for i in xrange(n):
		print "X",i,": ",X[i]

##########################################################################################################################################
def GaussE(A,n,B,p):
	X = [0.0 for i in range(n)]
	for k in xrange(n-1):
		if(p):
			A,B = pivot(A,k,n,B)
		#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
		#print A,B
		for i in xrange(k+1,n):
			c = float(A[i][k]/A[k][k])
			for j in xrange(n):
				A[i][j] = A[i][j]-A[k][j]*c
			B[i] = B[i] - B[k]*c
			#print "####################################"
			#print A,B

	#print A,B
	#backtracing
	for i in xrange(n-1,-1,-1):
		X[i] = B[i]/A[i][i]
		for j in xrange(n):
			B[j] = B[j] - X[i]*A[j][i]
	#print B,X

	pr(A,B,X)

########################################################################################################################################
def GaussJ(A,n,B):
	for k in xrange(n-1):
		A,B = pivot(A,k,n,B)
		for i in xrange(k+1,n):
			c = float(A[i][k]/A[k][k])
			for j in xrange(n):
				A[i][j] = A[i][j]-A[k][j]*c
			B[i] = B[i] - B[k]*c
			#print A,B

	for k in xrange(1,n):
		for i in xrange(k):
			c = float(A[i][k]/A[k][k])
			for j in xrange(i,n):
				A[i][j] = A[i][j]-A[k][j]*c
			B[i] = B[i] - B[k]*c

	#print A,B

	for i in range(n):
		B[i] = B[i]/A[i][i]
		#A[i][i] = 1.0

	#print A,B
	pr(A,B,B)

##################################################################################################################################################
print "Enter coeff matrix size"
n = int(raw_input().strip())

print "Enter Coef Matrix"

A=[]
for x in xrange(n):
	a = map(float,raw_input().strip().split(' '))
	A.append(a)
print A
f=0
for i in range(n):
	f=0
	for j in range(n):
		if(A[j][i]!=0):
			f=1
			break
	if(f==0):
		print "Singular Matrix, Inverse do not exist"
		break

if(f!=0):
	print "Enter Vector B"
	B = map(float,raw_input().strip().split(' '))

	print "Enter 2 for Gauss Jordan Method ,1 for Gauss Elimination with pivoting and 0 for without pivoting"
	z = int(raw_input().strip())

	print "The matrix A and vector B"
	print "==================="
	print A,B

	if(z==2): 
		GaussJ(A,n,B)
	elif(z==1):
		GaussE(A,n,B,1)
	elif(z==0):
		GaussE(A,n,B,0)	
	else:
		print "Not Valid Input"

##############################################################################
print "Do you want to enter again"
l = raw_input().strip()
while((l[0]=='y') or (l[0]=='Y')):
	print "Enter coeff matrix size"
	n = int(raw_input().strip())

	print "Enter Coef Matrix"

	A=[]
	for x in xrange(n):
		a = map(float,raw_input().strip().split(' '))
		A.append(a)
	print A
	f=0
	for i in range(n):
		f=0
		for j in range(n):
			if(A[j][i]!=0):
				f=1
				break
		if(f==0):
			print "Singular Matrix, Inverse do not exist"
			break

	if(f!=0):
		print "Enter Vector B"
		B = map(float,raw_input().strip().split(' '))

		print "Enter 2 for Gauss Jordan Method ,1 for Gauss Elimination with pivoting and 0 for without pivoting"
		z = int(raw_input().strip())

		print "The matrix A and vector B"
		print "==================="
		print A,B

		if(z==2): 
			GaussJ(A,n,B)
		elif(z==1):
			GaussE(A,n,B,1)
		elif(z==0):
			GaussE(A,n,B,0)	
		else:
			print "Not Valid Input"
	print "Do you want to enter again"
	l = raw_input().strip()
###########################################################################################################################################################

'''
3.01 2.22 4.1
1.00 3.21 5.3
0.3 -0.44 6.6

4.5 5.1 7.1
'''

'''
2.54 1.3 2.1
0.00002 1.5 -4.3
3.1 6.1 14.2

4.4 3.33 7.22
'''