import os
import sys
files=os.listdir(sys.argv[1])
def countfiles(files):
	return [f for f in files if '.py' in f]
print len (countfiles(files))
