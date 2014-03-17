x=[5,3,3,4,7]
def cumulativ_sum(l):
	e=[]
	for i in range(1,len(l)+1):
		e.append(sum(l[0:i]))
	print e
cumulativ_sum(x)
	
