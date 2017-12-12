#!/usr/bin/env python2
#-*- coding:utf-8 -*- 

""" sum of four number 

# 排序 -> 搜索（DFS）-> 剪枝
"""

def find_target_list(num_list,target,K,start_pos,end_pos):
	if target == 0 and K == 0:
		return [[]]
	if K == 0:
		return None
	if (end_pos - start_pos + 1) < K:
		return None
	if K > 0 and num_list[start_pos] > target:
		return None
	ret_list = []
	for ind in range(start_pos,end_pos+1):
		cur_elem = num_list[ind]
		r_list = find_target_list(num_list,target - cur_elem,K-1,ind+1,end_pos)
		if r_list is None:
			continue
		for r in r_list:
			c_ret_list = [cur_elem]
			c_ret_list.extend(r)
			ret_list.append(c_ret_list)	
	return ret_list


def sum_of_four_number(num_list,target):
	""" """
	num_list = sorted(num_list)
	print num_list
	r_list = find_target_list(num_list,target,4,0,len(num_list)-1)
	print(r_list)
	for e in r_list:
		print e
	

a = [1, 0, -1, 0, -2, 2]
print sum_of_four_number(a,0)


















