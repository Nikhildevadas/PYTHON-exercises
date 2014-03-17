import os
import sys
import urllib
import re
url=sys.argv[1]
if url[-1]=='/':
	basename='index.html'
else:
	basename=url.split('/')[-1]
print 'Saving  ',url,'  as ',basename
urllib.urlretrieve(url,os.getcwd()+'/'+basename)
f=open(basename,'r')
a=re.findall(r'>[^<]+<',f.read())
for i in a:
	print i[1:-1]

