import sys
import math
import copy

'''
=============================================
! Lab No: 6
! Title : differencial
! Date: 3/9/2017
! Name : Parismita Das
! Roll No: 150121031
!Email : parismita@iitg.ernet.in
============================================='''
######################__eqn__#############################
def eqn(x,y):
	a = -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1
	return a

######################__slope__#############################
def eqn(x,y):
	a = -2*x**3 + 12*x**2 -20*x + 8.5
	return a

######################__slope__#############################
def error(y,y1,n):
	a = [0.0 for i in range(n+1)]
	for i in xrange(n+1):
		a[i] = (y[i]-y1[i])/y1[i]*100
	#print a
	return a

######################__heun__#############################
def Heun(x,step,n,m):
	yheun = [1.0 for i in range(n+1)]
	for i in xrange(n):
		yheun[i+1] = yheun[i]+step*(m[i]+m[i+1])/2
	#print yheun
	return yheun
'''
yi+1 = yi + h*mi
yi+1 = yi + h/2(mi+1+mi)
'''

######################__euler__#############################
def Euler(x,step,n,m):
	yeuler = [1.0 for i in range(n+1)]
	for i in xrange(n):
		yeuler[i+1] = yeuler[i]+step*(m[i])
	#print yeuler
	return yeuler

#####################___Main__Prog__##########################
start = 0
end = 4
step =0.5
n = int((end-start)/step)

x = [w * step for w in range(n+1)]
x4 = [1.0 for i in range(n+1)]
x3 = [1.0 for i in range(n+1)]
x2 = [1.0 for i in range(n+1)]
yexact = [1.0 for i in range(n+1)]
m = [1.0 for i in range(n+1)]

#print "x"
for i in xrange(n+1):
	x4[i] = x[i]**4
	x3[i] = x[i]**3
	x2[i] = x[i]**2
	#print x[i]

for i in xrange(n+1):
	yexact[i] = -0.5*x4[i] + 4*x3[i] - 10*x2[i] + 8.5*x[i] + 1
	m[i] = -2*x3[i] + 12*x2[i] -20*x[i] + 8.5

#print yexact
yheun = Heun(x,step,n,m)
yeuler = Euler(x,step,n,m)
eh = error(yheun,yexact,n)
ee = error(yeuler,yexact,n)

print "         x           yexact         yheun         eheun         yeuler         eeuler"
for i in xrange(n+1):
	line_new = '{:>12}  {:>12}  {:>12} {:>16}  {:>12} {:>16}'.format(x[i],yexact[i],yheun[i],eh[i],yeuler[i],ee[i])
	print line_new


f=open('output.txt','w')
for i in range(n+1):
	f.write(str(i*step))
	f.write(" ")
	f.write(str(yexact[i]))
	f.write(" ")
	f.write(str(yheun[i]))
	f.write(" ")	
	f.write(str(eh[i]))
	f.write(" ")	
	f.write(str(yeuler[i]))
	f.write(" ")	
	f.write(str(ee[i]))
	f.write("\n")
#p "output.txt"u 1:2 w lp,"output.txt"u 1:3 w lp,"output.txt"u 1:4 w lp,"output.txt"u 1:5 w lp,"output.txt"u 1:2 w lp, "output.txt"u 1:6 w lp
#p "output.txt"u 1:2 w lp,"output.txt"u 1:3 w lp,"output.txt"u 1:5 w lp,"output.txt"u 1:2 w lp

#error forluma = h^m/(m+1)! [y^m(x+h) - y^m(x)]
#rk2
#heun a1=a2=1/2, p1=p2=1   y[i+1] = yi + (k1+k2)/2*h  ki = f(x,y) k2= f(x+h,y+k1*h)
#euler a1=1 a2=0 yi+1 = yi +k1h k1=f(x,y)
#midpoint a1=0 a2=1 p1=p2=1/2 y[i+1] = yi + k2h  k2 = f(x+h/2,y+h/2)
