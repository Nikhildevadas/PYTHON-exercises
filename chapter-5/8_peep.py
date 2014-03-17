def peep(it):
	p=it.next()
	l=[]
	l.append(p)
	l.extend(list(it))
	it1=iter(l)
	return p,it1
it = iter(range(5))
x,it1=peep(it)
print x,list(it1)

