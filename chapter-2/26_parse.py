def parse(a,b,c):
	f=open(a).readlines()
	w=[]	
	for i in f:
		if i[0]!="#":
			w.append(i[:-1].split(b))
	return w	
print parse("a.txt","!","#")
