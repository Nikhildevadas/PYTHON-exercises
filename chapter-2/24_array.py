import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
def array(a,b):
	return[[None]*b for i in range(a)]

print array(a,b)

