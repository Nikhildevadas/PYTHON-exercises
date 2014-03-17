def group(list,size):
	return [list[i:i+size] for i in range(0,len(list),size)]
print group([2,3,4,5,6,2,34,5,6,6,1],3)
		
