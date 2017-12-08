#!/usr/bin/env python2
#-*- coding:utf-8 -*-



def trapping_watter_1(list_):
	
	#find the top
	top = max(list_)
	
	#水是形成塔型 https://www.cnblogs.com/felixfang/p/3713197.html
	cur_top = 0
	area = 0
	start_pos,end_pos = -1,-1
	for start_pos in range(len(list_)):
		elem = list_[start_pos]
		if elem == top:
			break
		if elem > cur_top:
			cur_top = elem
			continue
		area += (cur_top - elem)
	cur_top = 0
	for end_pos in range(len(list_))[::-1]:
		elem = list_[end_pos]
		if elem == top:
			break
		if elem > cur_top:
			cur_top = elem
			continue
		area += (cur_top - elem)
		
	for pos in range(start_pos,end_pos):
		elem = list_[end_pos]
		area += (start_pos - elem)
	
	return area

a = [0,1,0,2,1,0,1,3,2,1,2,1]
print trapping_watter_1(a)
