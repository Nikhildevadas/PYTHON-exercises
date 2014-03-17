import sys
import os
def extcount(filenames):
	dict={}
	for filename in filenames:
		dict[filename.split('.')[1]]=dict.get(filename.split('.')[1],0)+1
	return dict
dir=sys.argv[1]
filenames=os.listdir(os.path.abspath(dir))
dict=extcount(filenames)
for i,j in dict.items():
	print i,j
