def lensort(list):
	return sorted(list,key=lambda x:len(x))
print lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
