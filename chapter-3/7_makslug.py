import re
def mak_slug():
	a=re.findall(r'\w+',string)
	print ('_').join(a)
string=raw_input("enter string") 
mak_slug()
