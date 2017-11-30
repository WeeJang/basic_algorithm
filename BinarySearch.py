#!/usr/bin/env python2
#-*- coding:utf-8 -*-



# Template
def binary_search(elem_list,target):
	if len(elem_list) == 0:
		return -1
	start,end = 0,len(elem_list) - 1
	while start + 1 < end:
		mid = start + (end-start) / 2
		if elem_list[mid] > target:
			end = mid
		else:
			start = mid
	if elem_list[start] == target:
		return start
	elif elem_list[end] == target:
		return end
	else:
		return -1	
	

# find min roarted-array
def find_min(elem_list):
	
	start,end = 0,len(elem_list)-1
	target = elem_list[-1]
	
	while start + 1 < end:
		mid = start + (end - start) / 2
		if elem_list[mid] < target:
			end = mid
		else:
			start = mid
	print "==>",elem_list[start:end+1]
	if elem_list[start] < target:
		return elem_list[start]
	else:
		return elem_list[end]


test = [5,6,7,8,0,1,2]
test = [5,6,7,8,0]
print find_min(test)					
	








