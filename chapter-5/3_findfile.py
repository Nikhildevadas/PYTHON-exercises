import os
def findfile(direc):
	files=os.listdir(direc)
	for i in files:
		print os.path.abspath(direc+'/'+i)
		if os.path.isdir(os.path.abspath(direc+'/'+i)) is True:
			findfile(direc+'/'+i)
findfile('2')
