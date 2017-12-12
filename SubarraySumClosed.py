#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 数组中某一个区间的和接近0 """
""" 分析问题: Sum[i,j] = Sum[0,j] - sum[0,i-1]
	转化为前缀和.(区间和->前缀和)
    sum[i,j] -> 0,means 找到两个前缀和够接近
    排序即可解决
"""

def cal_prefix_sum(num_list):
	prefix_sum = [ 0 for i in range(len(num_list)) ]
	for i in range(len(num_list)):
		elem = num_list[i]	
		if i == 0:
			prefix_sum[i] = elem
		else:
			prefix_sum[i] = elem + prefix_sum[i-1]
	prefix_sum_dict = {}
	for i in range(len(prefix_sum)):
		prefix_sum_dict[i] = prefix_sum[i]
	sorted_prefix_sum_list = sorted(prefix_sum_dict.iteritems(),key = lambda x:x[1])
	return sorted_prefix_sum_list

def find_closed_elem(prefix_sum):
	ret_index = -1
	last_gap = float("inf")
	for i in range(1,len(prefix_sum)):
		gap = abs(prefix_sum[i][1] - prefix_sum[i-1][1])
		if gap < last_gap:
			ret_index = i
			last_gap = gap
	print ret_index,prefix_sum
	i,j = prefix_sum[ret_index][0],prefix_sum[ret_index-1][0]
	return [i+1,j]
			
a = [1,5,-7,2,3,10]
b = cal_prefix_sum(a)	
print find_closed_elem(b)


























