# -*- coding:utf-8 -*-
from functools import reduce
def prod(L):
	def fn(x,y):
		return x*y
	return reduce(fn,L)
print(prod([3,5,7,9]))