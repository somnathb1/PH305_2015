import math
import copy

'''
=============================================
! Lab No: 9
! Title : finite diff
! Date: 24/10/2017
! Name : Parismita Das
! Roll No: 150121031
!Email : parismita@iitg.ernet.in
============================================='''
################################################____Finite_diff____##########################################

def fdiff(n,h,hp,Ta):
	T=[0 for i in range(n+1)]
	T[0]=40
	T[n]=200
	M=[[0 for i in range(n-1)] for j in range(n-1)]
	temp=[-1,2+hp*h*h,-1]
	#MT=B
	B=[hp*h*h*Ta for i in range(n-1)]
	B[0]+=T[0]
	B[n-2]+=T[n]
	
	for i in range(n-1):
		for j in range(n-1):
			if i==j:
				M[i][j]=temp[1]				
			if i==j+1:
				M[i][j]=temp[0]				
			if i==j-1:
				M[i][j]=temp[2]	
	
	M,B=guass(M,B,n-1)
	
	for i in range(n-1):
		T[i+1]=B[i]/M[i][i]	
	
	return M,B,T		
	

################################################____Shooting_method____#########################################

def shoot(n,h,hp,Ta):
										#use rk4 to solve shoot	
	Y1,Z1=rk4(n,h,0)
	Y2,Z2=rk4(n,h,50)
										#interpolation
	x=((50)*(200-Y1[n]))/(Y2[n]-Y1[n])
	Y,Z=rk4(n,h,x)
	return Y
	

#################################################___RK_4___##########################################

def rk4(n,h,t):
	Y=[0.0 for i in range(n+1)]
	Z=[0.0 for i in range(n+1)]
	Y[0]=40.0
	Z[0]=t								#Set trial
	k11=k21=k31=k41=0
	k12=k22=k32=k42=0
	for i in range(n):
	
		k11=func1(i*h,Y[i],Z[i])
		k12=func2(i*h,Y[i],Z[i])
				
		y=copy.deepcopy(Y[i])
		y+=k11*h/2		
		z=copy.deepcopy(Z[i])
		z+=k12*h/2		

		k21=func1((i+0.5)*h,y,z)
		k22=func2((i+0.5)*h,y,z)

		y=copy.deepcopy(Y[i])
		y+=k21*h/2		
		z=copy.deepcopy(Z[i])
		z+=k22*h/2		

		k31=func1((i+0.5)*h,y,z)
		k32=func2((i+0.5)*h,y,z)

		y=copy.deepcopy(Y[i])
		y+=k31*h		
		z=copy.deepcopy(Z[i])
		z+=k32*h		
		
		k41=func1((i+1)*h,y,z)
		k42=func2((i+1)*h,y,z)
		
		Y[i+1]=Y[i]+h/6*(k11+2*k21+2*k31+k41)
		Z[i+1]=Z[i]+h/6*(k12+2*k22+2*k32+k42)
					
	return Y,Z




#################################################___Rk4_func1___##########################################

def func1(x,y,z):
	hp=0.01
	Ta=20
	my=z
	return my

#################################################___Rk4_func2___############################################

def func2(x,y,z):
	hp=0.01
	Ta=20		
	mz=(y-Ta)*hp	
	return mz

############################################################################################################
def guass(M,B,n):
	MM=copy.deepcopy(M)
	BB=copy.deepcopy(B)
	for i in range(n):
		for j in range(n):
			if i!=j:			
				c=MM[j][i]/MM[i][i]
				for p in range(i,n):
					MM[j][p]=MM[j][p]-MM[i][p]*c
				BB[j]=BB[j]-c*BB[i]	
	return MM,BB


##################################################____Main____#######################################

print "\nPlease enter number of points for plotting:   "
#n=int(raw_input().strip())
n=10
h=10.0/n
hp=0.01
Ta=20

M,B,T=fdiff(n,h,hp,Ta)
print "\n "
print "\n--------------------------------------Finite difference------------------------------------------------"
#print "\n Matrix "
#print('\n'.join([''.join(['{:25}'.format(round(item, 6)) for item in row])for row in M]))
#print "\n ",B
print "\n\nThe solution in Celcius "
for x in xrange(n+1):
	print T[x]
print "\n--------------------------------------Shooting method------------------------------------------------"

Ts=shoot(n,h,hp,Ta)
print "\n\nThe solution in Celcius "
for x in xrange(n+1):
	print Ts[x]
print "\n "

#---------------------------------output-------------------------------------------------------------------------
f=open('output.txt','w')
for i in range(n+1):
	#f.write(str(i))
	#f.write(" ")
	f.write(str(T[i]))
	f.write(" ")
	f.write(str(Ts[i]))
	f.write("\n")

# p "output.txt" u 1:1 w lp, "output.txt"u 1:2 w lp

print "\n-------------------------------------------root mean square difference-----------------------------------"
s=0
for x in xrange(n):
	s += (T[x]-Ts[x])**2 

print s**0.5*100,"%"


'''
eqn
fd y'' = y(x+2h)-2y(x+h)+y(x)/h2
bd y'' = y(x)-2y(x-h)+y(x-2h)/h2
cd y'' = y(x+h)-2y(x)+y(x+h)/h2

put y''= f(x,y)