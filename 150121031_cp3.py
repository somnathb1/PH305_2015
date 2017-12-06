import sys
import copy

filename = 'a.txt'
input_filename=open(filename)
with input_filename as f:
	inp = f.readlines()
inp = [x.strip().split(" ") for x in inp]	

n=int(inp[0][0])
A=[]
A = [[0 for i in range(n)] for j in range(n)]
for i in range(n+1):
	if i!=n:		
		A[i]=map(float, inp[i+1])
	if i==n:
		B=map(float, inp[i+1])		
#####################___Guass_Seidel___#########################
def gs(tolerance):
	X=[0.0 for i in range(n)]
	temp=[0.0 for i in range(n)]
	z=0	
	
	while i!=3:
		z=z+1		
		i=0
		temp=copy.deepcopy(X)		

		for j in range(n):
			temp[j]=B[j]	
			for k in range(n):
				if k!=j:
					temp[j]=temp[j]-A[j][k]*temp[k]		
			temp[j]=temp[j]/A[j][j]
				
		for l in range(n):
			if (abs(temp[l]-X[l])<tolerance):
				i=i+1	
		X=temp
		print "\n The order of iteration is  ",z
		print "The solution at this stage is", X

	print "\nThe solution is :"
	print X
	print "\n"
	
#####################___Jacobi___#########################

def jacobi(tolerance):
	X=[0.0 for i in range(n)]
	temp=[0.0 for i in range(n)]
	z=0	
	
	while i!=3:
		z=z+1		
		i=0
		temp=copy.deepcopy(X)		

		for j in range(n):
			temp[j]=B[j]	
			for k in range(n):
				if k!=j:
					temp[j]=temp[j]-A[j][k]*X[k]		
			temp[j]=temp[j]/A[j][j]
				
		for l in range(n):
			if (abs(temp[l]-X[l])<tolerance):
				i=i+1	
		X=temp
		print "\n The order of iteration is  ",z
		print "The solution at this stage is", X

	print "\nThe solution is :"
	print X
	print "\n"	

#####################___Main__Prog__##########################

print "\nPlease choose method"
print "Enter 1 for Guass-Seeidel and 2 for Jacobi"
x=int(raw_input().strip())
print "\nPlease enter the tolerance you require"
y=int(raw_input().strip())
z=1.0000000000000
for i in range(y):
	z=z/10
if x==1:
	gs(z)
if x==2:
	jacobi(z)


