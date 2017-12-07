#!/usr/bin/env python2
#-*- coding:utf-8 -*- 

""" 最大乘积子序列 """

def get_max_multi_array(list_):
	
	cur_max,cur_min = 1,1
	max_result = cur_max
	
	for elem in list_:
		a,b = cur_max*elem,cur_min*elem
		cur_max = max(a,b,elem)
		cur_min = min(a,b,elem)
		if cur_max > max_result:
			max_result = cur_max 

	return max_result		


a = [2,1,-5,6,-2]

print get_max_multi_array(a)
