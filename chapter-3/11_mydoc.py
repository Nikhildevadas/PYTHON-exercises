import sys
__import__(sys.argv[1])
print "help on module",sys.argv[1]
print "DESCRIPTION"
print __import__(sys.argv[1]).__doc__
print "FUNCTIONS"
for i in dir(sys.argv[1]):
	print i

