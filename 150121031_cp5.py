import sys
import math
import copy

'''
=============================================
! Lab No: 5
! Title : Harmonic Oscilator
! Date: 3/9/2017
! Name : Parismita Das
! Roll No: 150121031
!Email : parismita@iitg.ernet.in
============================================='''


######################__max elem__#############################
def maxelem(H,n):
	l = 0
	k = 0
	ma = 0.0
	for i in xrange(n):
		for j in xrange(n):
			if(i!=j):
				if(abs(H[i][j])>abs(ma)):
					ma=H[i][j]
					l = i
					k = j
	return ma,l,k

######################__power__#############################
def rotate(H,n,p,q):
	D = copy.deepcopy(H)
	theta = (H[q][q] - H[p][p])/(2*H[p][q])
	if(theta>=0.0):
		t = 1.0/(abs(theta) + math.sqrt(theta*theta + 1.0))
	else:
		t = -1.0/(abs(theta) + math.sqrt(theta*theta + 1.0))
	c = 1.0/math.sqrt(t*t + 1.0)
	s = t*c
	tau = s/(1.0 + c)


	D[p][q] = 0.0
	D[q][p] = 0.0
	D[p][p] = c*c*H[p][p]+s*s*H[q][q]-2*s*c*H[p][q]
	D[q][q] = s*s*H[p][p]+c*c*H[q][q]+2*s*c*H[p][q]
	for i in xrange(n):
		if((i!=p)and (i!=q)):
			D[i][p] = c*H[i][p] - s*H[i][q]
			D[p][i] = D[i][p]
			D[q][i] = s*H[i][p] + c*H[i][q]
			D[i][q] = D[q][i]

	'''for i in range(n):
		temp = R[i][l]
		R[i][l] = temp - s*(R[i][k] + tau*R[i][l])
		R[i][k] = R[i][k] + s*(temp - tau*R[i][k])'''
	
	return D


######################__power__#############################
def jakobi(H,n,tol=1.0e-20):

	R = [[0.0 for i in range(n)]for j in range(n)]    # Initialize transformation matrix
	for i in xrange(n):
		R[i][i]=1.0

	for i in range(5*(n*n)): # Jacobi rotation loop 
		m,p,q = maxelem(H,n)
		if abs(m) < tol:
			break
		H=rotate(H,n,p,q)

	print "D updated:"
	for i in xrange(n):
		print H[i]
	'''print "\nR updated:"
	for i in xrange(n):
		print R[i]'''
	return H


#####################___Main__Prog__##########################
n=5
f=open('output.txt','w')
H = [[0.0 for i in range(n)] for j in range(n)]
x = [[0.0 for i in range(n)] for j in range(n)]
for i in xrange(1,n):
	H[i-1][i-1]=float(2*i-1)/2
	x[i][i-1]= math.sqrt(i)/math.sqrt(2)
	x[i-1][i]= math.sqrt(i)/math.sqrt(2)
H[n-1][n-1]=float(2*n-1)/2

print "#################################################"
print "Ho:"
for i in xrange(n):
	print H[i]
print "#################################################"
print "x"
for i in xrange(n):
	print x[i]

x = [[sum(a*b for a,b in zip(A_row,Ai_col)) for Ai_col in zip(*x)] for A_row in x]  #1*1
x = [[sum(a*b for a,b in zip(A_row,Ai_col)) for Ai_col in zip(*x)] for A_row in x]  #2*2
print "#################################################"
print "H:"
for j in xrange(n):
	print x[j]

lamb = [w * 0.1 for w in range(0, 11)]
for z in lamb:
	K = copy.deepcopy(H)
	for i in xrange(n):
		for j in xrange(n):
			H[i][j]= H[i][j]+x[i][j]*z

	print "#################################################"
	print "H(total):"
	for j in xrange(n):
		print H[j]
	#-----------------------------------------------------
	H = jakobi(H,n)
	E = [0 for o in range(n)]
	for j in range(n):
		E[j]=H[j][j]
	E.sort()
	for j in range(n):
		f.write(" ")
		f.write(str(E[j]))
	f.write("\n")
	H = copy.deepcopy(K)

	
	print "good bye"
'''

H = [[4.0, -30.0, 60.0, -35.0 ],
[-30.0, 300.0 ,-675.0 ,420.0],
[60.0, -675.0, 1620.0, -1050.0],
[-35.0 ,420.0, -1050.0, 700.0]]
H = jakobi(H,n)
print "good bye"#'''

#p "output.txt"u 1:2 w lp,"output.txt"u 1:3 w lp,"output.txt"u 1:4 w lp,"output.txt"u 1:5 w lp,"output.txt"u 1:2 w lp, "output.txt"u 1:6 w lp