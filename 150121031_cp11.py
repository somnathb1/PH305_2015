import math
import copy

'''
=============================================
! Lab No: 10
! Title : integral
! Date: 7/11/2017
! Name : Parismita Das
! Roll No: 150121031
!Email : parismita@iitg.ernet.in
============================================='''

###############################################################################################################

def func(x,a,b):
	f_x=0.2+25*x-200*x**2+675*x**3-900*x**4+400*x**5
	return f_x

###############################################################################################################

def trap(a,b):
	I=(b-a)*(func(a,a,b)+func(b,a,b))*0.5
	return I

###############################################################################################################

def trap_m(X,n,a,b):
	summ=0
	for i in range(n-1):
		summ+=func(X[i+1],a,b)
	I=(b-a)*(func(a,a,b)+func(b,a,b)+2*summ)/2/n
	return I

###############################################################################################################

def randm(x):
	x=x*100
	a=69
	c=15
	m=80
	xx=(a*x+c)%m
	return xx/100

###############################################################################################################

def smean(n,a,b):
	XX=[0.0 for i in range(n+1)]
	XX[0]=0.4			#	Guess value	
	for i in range(n):
		XX[i+1]=randm(XX[i])
	#print "\nPrinting X(smean)", XX	,"\n\n"
	temp=0
	for i in range(1,n+1):
		temp+=func(XX[i],a,b)	
	temp=temp/n
	I=(b-a)*temp
	return I	

###############################################################################################################

a=0
b=0.8
print "\nPlease enter number of points to be plotted"
n=int(raw_input().strip())
X=[0.0 for i in range(n+1)]
h=(b-a)/n
print "\n Printing n", n

for i in range(n+1):
	X[i]=a+i*h

#print "\nPrinting x values", X

print "\n\nIntegral from trapezoid : ", trap(a,b)
print "\n\nIntegral from trapezoid multiple : ", trap_m(X,n,a,b)
print "\n\nIntegral from sample mean : ", smean(n,a,b), "\n"

'''
f = sum Lif(xi)
Li = product x-xj/xi-xj i!=j

simson
i = h/3[f(x0)+4f(x1)+f(x2)] h = b-a/2   x1=b+a/2
error = -h**5/90*f4(x)  2580 180

milti simson
4*f odd xi 
2*f even xi
fo and fn ka h/3
error

trap 2d
y0 y1 y2 x0 x1 x2
y0  -> trap_m(x) (b1-a1)
y1 y2 same
trap (y0 y1 y2) (b2-a2)

pi code
xi yi random gen
x2+y2<radius r=1 yes->o++
x=(0,1) y=(0,1)
o/array size = pi/4

<f> = 1/nsum(f(xi))
I = b-a<f>

2d f(x,y)dxdy
(b1-a1)(b2-a2)
'''