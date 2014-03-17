import sys
import os
dir=sys.argv[1]
filenames=os.listdir(os.path.abspath(dir))
for filename in filenames:
	print filename,'\t',len(open(os.path.abspath(dir + "/" + filename)).readlines()), '\t',os.stat(os.path.abspath(dir +"/" + filename))[8]
	


