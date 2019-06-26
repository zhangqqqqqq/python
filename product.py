# -*- coding: utf-8 -*- 
def product(x,*numbers):
	sum=1
	for n in numbers:
		sum=sum*n
	return x*sum
print(product(),product(1,2),product(1,2,3))