f=open('tex.txt').readlines()
k=len(max(f))
for i in f:
	h=k-len(i)/2
	print " "*h+i
