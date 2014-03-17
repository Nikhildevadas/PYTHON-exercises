import sys
f=open(sys.argv[1]).readlines()
k=int(sys.argv[2])
for i in f:
	new=i
	if len(new)>k:
		if new[k]==" ":
			print new[:k]
			print new[k:]
		else:
			for a in new[k:]:
				if a==' ':				
					j=new[k:].index(a)
					print new[:j+len(new[:k])]
					print new[j+len(new[:k]):]
					break
					
