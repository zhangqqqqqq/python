# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
	s1,s2=s.split('.')
	digital={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
	def fn(x,y):
		return 10*x+y
	def char2num(s):
		return digital[s]
	return reduce(fn,map(char2num,s1))+reduce(fn,map(char2num,s2))/(pow(10,len(s2)))
print(str2float('123.688'))
if abs(str2float('123.688')-123.688)<0.00001:
	print('成功')
else:
	print('失败')