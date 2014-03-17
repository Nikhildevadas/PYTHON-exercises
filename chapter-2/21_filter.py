def filter(f,l):
	return[x for x in l if even(x) is True]
def even(r):
	return r%2==0
l=[1,2,3,4]
print filter(even,l)
