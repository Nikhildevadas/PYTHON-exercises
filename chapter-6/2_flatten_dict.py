def flatten_dict(a,result=None):
	if result==None:
		result={}
	t={}
	for k,v in a.items():
		if isinstance(v,dict):
			for i,j in v.items():
				t[k+"."+i]=j		
			flatten_dict(t,result)
		else:
			result[k] = v
	return result
print flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
