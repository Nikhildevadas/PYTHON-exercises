import sys
import re
import urllib
url=sys.argv[1]
a=urllib.urlopen(url)
b=re.findall(r'http://[\S\s]+',a.read())
for i in b:
	print i[:-1]

