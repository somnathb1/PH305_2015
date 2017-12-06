import math
import copy

'''
=============================================
! Lab No: 9
! Title : fitting
! Date: 24/10/2017
! Name : Parismita Das
! Roll No: 150121031
!Email : parismita@iitg.ernet.in
============================================='''

##############################################################################################################

def Uab(x,a,b,l):
	U=0.0
	for i in range(l):
		U+=x[i]**(a+b)
	return U	

##############################################################################################################

def Va(x,y,a,l):
	V=0.0
	for i in range(l):
		V+=y[i]*x[i]**a
	return V	

##############################################################################################################

def MV(x,y,n,l):
	M=[[0.0 for i in range(n)] for j in range(n)]
	V=[0.0 for i in range(n)]
	for i in range(n):
		V[i]=Va(x,y,i,l)
	for i in range(n):
		for j in range(n):
			M[i][j]=Uab(x,i,j,l)
	return M, V				 

##############################################################################################################

def guass(M,V,n):
	MM=copy.deepcopy(M)
	BB=copy.deepcopy(V)
	for i in range(n):
		for j in range(n):
			if i!=j:			
				c=MM[j][i]/MM[i][i]
				for p in range(i,n):
					MM[j][p]=MM[j][p]-MM[i][p]*c
				BB[j]=BB[j]-c*BB[i]	
	return MM,BB

##############################################################################################################

def func(x,ai,l):
	y_final=[0.0 for i in range(l)]
	for i in range(l):
		y_final[i] = ai[0]+ai[1]*x[i]+ai[2]*x[i]**2
	return y_final	


##############################################################################################################

file=open("input.txt")
with file as f:
	inp = f.readlines()
inp = [x.strip().split(" ") for x in inp]
x=map(float,inp[0])
y=map(float,inp[1])
l=len(x)
n=3
M,V = MV(x,y,n,l)
M,V = guass(M,V,n)
ai=[0.0 for i in range(n)]
for i in range(n):
	ai[i]=V[i]/M[i][i]
y_final=func(x,ai,l)
print '\n\nFinal y before fitting', y
print '\n\nCoeffficients', ai
print '\n\nFinal y after fitting', y_final, '\n\n'

##############################################################################################################


# p "output.txt" u 1:2 w lp, "output.txt"u 1:3 w lp
'''f(x)=a*x*x+b*x+c
fit f(x) "fitting"u 1:2 via a,b,c'''

bi = [2.47857 ,2.35929,1.86071]
y_finali=func(x,bi,l)

f=open('output.txt','w')
for i in range(l):
	f.write(str(x[i]))
	f.write(" ")
	f.write(str(y[i]))
	f.write(" ")
	f.write(str(y_final[i]))
	f.write(" ")
	f.write(str(y_finali[i]))
	f.write("\n")
