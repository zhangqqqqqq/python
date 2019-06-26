# -*- coding: utf-8 -*-
def findMinAndMax(L):
	if L==[]:
		return (None, None)
	else:
		max=L[0]
		min=L[0]
		for x in L:
			if x<min:
				min=x
			if x>max:
				max=x
		return (min,max)
print(findMinAndMax([7,1,3,9,5]))
        