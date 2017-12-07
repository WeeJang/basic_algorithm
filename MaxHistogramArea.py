#!/usr/bin/env python2
#-*- coding:utf-8 -*-


""" 单调栈 
1) 栈中元素 是升序。
2）如果待入栈元素 大于栈顶元素，则直接入栈；等于可忽略；小于栈顶元素则不断弹栈，直到满足条件。
"""

def get_max_histogram_area(height_list):
	
	target_result = (0,None)
	inc_stack = [] #升序栈 0:栈底 -1:栈顶
	height_list.append(0) #dummy
	for ind in range(len(height_list)):
		print inc_stack,
		cur_elem = height_list[ind]	
		print "process,",cur_elem
		if len(inc_stack) == 0:
			inc_stack.append(ind)
			continue
		if cur_elem == height_list[inc_stack[-1]]:
			continue
		elif cur_elem > height_list[inc_stack[-1]]:
			inc_stack.append(ind)
		else:
			while height_list[inc_stack[-1]] > cur_elem:
				j = inc_stack.pop()
				low_height = height_list[j]
				if len(inc_stack) != 0:
					i = inc_stack[-1]
				else:
					i = -1
				area = low_height * (j-i) 
				print(area,i,j)
				if area > target_result[0]:
					target_result = (area,(i,j))
				if len(inc_stack) == 0:
					break
			inc_stack.append(ind)
	return target_result	
				
a = [2,1,6,4,3]
print get_max_histogram_area(a)
	
	
