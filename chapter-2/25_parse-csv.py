f=open("a.csv").readlines()
k=[]
for i in f:
	k.append(i[:-1].split(","))
print k	
