# -*- coding:utf-8 -*-
def triangles():
	L1=[1]
	while True:
		yield L1
		L1=[1]+[L1[n-1]+L1[n]for n in range(1,len(L1))]+[1]
n=0
results=[]
for t in triangles():
	print(t)
	results.append(t)
	n=n+1
	if n==10:
		break