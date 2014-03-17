import sys
f=open(sys.argv[1]).readlines()
k=int(sys.argv[2])
for i in f:
	new=i
	while len(new)>k:
		print new[:k]
		new=new[k:]		
	print new
	
		
