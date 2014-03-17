def triplets(l):
	return[(x,y,z) for x in range(1,l) for y in range(x,l) for z in range(y,l) if x+y==z]
print triplets(5)
