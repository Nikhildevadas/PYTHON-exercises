import urllib
import json
print json.load(urllib.urlopen('http://httpbin.org/get'))['origin']
