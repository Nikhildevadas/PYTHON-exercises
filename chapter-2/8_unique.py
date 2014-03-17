def unique(x):
	n=[]
	for i in x:
		if i not in n:
			n.append(i)
print  unique([1,2,1,3,4,2,3])
