import os
import sys
dir=sys.argv[1]
filenames=os.listdir(os.path.abspath(dir))
for filename in filenames:
	print  filename
