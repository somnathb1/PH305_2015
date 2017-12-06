import math
import copy

'''
=============================================
! Lab No: 8
! Title : rk4
! Date: 10/10/2017
! Name : Parismita Das
! Roll No: 150121031
!Email : parismita@iitg.ernet.in
============================================='''
###############################################___Function_1___##########################################

def func1(x,y,z):
	m1=y*z+math.cos(x)-0.5*math.sin(2.0*x)
	return m1

###############################################___Function_2___##########################################

def func2(x,y,z):
	m2=z**2+y**2-(1+math.sin(x))
	return m2

###############################################___Heun___#############################################

def heun(n,h):
	Y=[0.0 for i in range(n+1)]
	Z=[0.0 for i in range(n+1)]
		
	Y[0]=0.0
	Z[0]=0.0
	
	for i in range(n):
		Y[i+1]=Y[i]+h*func1(i*h,Y[i],Z[i])
		Z[i+1]=Z[i]+h*func2(i*h,Y[i],Z[i])
		Y[i+1]=Y[i]+h/2*(func1(i*h,Y[i],Z[i])+func1((i+1)*h,Y[i],Z[i]))
		Z[i+1]=Z[i]+h/2*(func2(i*h,Y[i],Z[i])+func2((i+1)*h,Y[i],Z[i]))
	return Y,Z

##############################################____Euler___############################################

def euler(n,h):
	Y=[0.0 for i in range(n+1)]
	Z=[0.0 for i in range(n+1)]
	Y[0]=0.0
	Z[0]=0.0
	for i in range(n):
		Y[i+1]=Y[i]+h*func1(i*h,Y[i],Z[i])
		Z[i+1]=Z[i]+h*func2(i*h,Y[i],Z[i])
	return Y,Z 

#################################################___RK_4___##########################################
def rk4(n,h):
	Y=[0.0 for i in range(n+1)]
	Z=[0.0 for i in range(n+1)]
	Y[0]=0.0
	Z[0]=0.0
	k11=k21=k31=k41=0
	k12=k22=k32=k42=0
	for i in range(n):
	
		k11=func1(i*h,Y[i],Z[i])
		k12=func2(i*h,Y[i],Z[i])
				
		y=Y[i]
		y+=k11*h/2		
		z=Z[i]
		z+=k12*h/2		

		k21=func1((i+0.5)*h,y,z)
		k22=func2((i+0.5)*h,y,z)

		y=Y[i]
		y+=k21*h/2		
		z=Z[i]
		z+=k22*h/2		

		k31=func1((i+0.5)*h,y,z)
		k32=func2((i+0.5)*h,y,z)

		y=Y[i]
		y+=k31*h		
		z=Z[i]
		z+=k32*h		
		
		k41=func1((i+1)*h,y,z)
		k42=func2((i+1)*h,y,z)
		
		Y[i+1]=Y[i]+h/6*(k11+2*k21+2*k31+k41)
		Z[i+1]=Z[i]+h/6*(k12+2*k22+2*k32+k42)
					
	return Y,Z



###############################################___Main___##########################################

#print "\nPlease enter number of points for plotting:   "
#n=int(raw_input().strip())
#print "\n\nPlease enter step size:   "
#h=int(raw_input().strip())
start = 0
end = 2
n=24
h = float(end-start)/n

Y1,Z1=heun(n,h)
Y2,Z2=euler(n,h)
Y3,Z3=rk4(n,h)

print "         steps             yrk4            yheun            yeuler             zrk4            zheun            zeuler"
for i in xrange(n+1):
	line_new = '{:>16}  {:>16}  {:>16} {:>16}  {:>16} {:>16} {:>16} '.format(i*h,Y3[i],Y1[i],Y2[i],Z3[i],Z1[i],Z2[i])
	print line_new

f=open('output.txt','w')
for i in range(n):
	f.write(str(i*h))
	f.write(" ")
	f.write(str(Y3[i]))
	f.write(" ")
	f.write(str(Y1[i]))
	f.write(" ")	
	f.write(str(Y2[i]))
	f.write(" ")	
	f.write(str(Z3[i]))
	f.write(" ")
	f.write(str(Z1[i]))
	f.write(" ")	
	f.write(str(Z2[i]))
	f.write("\n")	
	
# p "output.txt" u 1:2 w lp, "output.txt"u 1:3 w lp, "output.txt"u 1:4 w lp, "output.txt" u 1:5 w lp,"output.txt" u 1:6 w lp, "output.txt"u 1:7 w lp
# p "output.txt" u 1:2 w lp, "output.txt"u 1:3 w lp, "output.txt"u 1:4 w lp
# p "output.txt" u 1:5 w lp,"output.txt" u 1:6 w lp, "output.txt"u 1:7 w lp
















