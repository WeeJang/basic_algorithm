#!/usr/bin/env python2
#-*- coding:utf-8 -*-
"""
你给出一个整数数组(size为n)，其具有以下特点：

相邻位置的数字是不同的
A[0] < A[1] 并且 A[n - 2] > A[n - 1]
假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。

"""

### 二分查找 ###


def find_peek(value_list):
	
	def helper(value_list,start_pos,end_pos):
		if start_pos >= end_pos - 1:
			return -1
		mid = start_pos + (end_pos - start_pos) / 2
		if value_list[mid] > value_list[mid-1] and value_list[mid] > value_list[mid+1]:
			return mid
		maybe_left = helper(value_list,start_pos,mid)
		if maybe_left != -1:
			return maybe_left
		return helper(value_list,mid+1,end_pos)
	
	return helper(value_list,0,len(value_list) - 1)


a = [1, 2, 1, 3, 4, 5, 7, 6]	
print find_peek(a)
