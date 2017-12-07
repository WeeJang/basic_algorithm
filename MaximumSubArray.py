#!/usr/bin/env python2
#-*- coding:utf-8 -*-



"""Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6."""


"""
 O(n)
"""

def get_max_subarray_sum_by_dp(list_):
	"""DP  解法 
	这个解法的抽象非常重要，也非常牛逼。就是这个L
	"""	
	#定义 L: L[i]为以第i元素（即list_[i]为末尾的子数组中最大的和）
	#则有 L[i+1] = max(L[i] + list_[i+1],list_[i+1])
	
	max_sum = -1
	L = -1
	for elem in list_:
		L = max(L + elem,elem)
		if L > max_sum:
			max_sum = L
	return max_sum		


def get_max_subarray_sum_by_dc(list_):
	""" 分治 解法
	这个的O(n*log*n)
	分析时间复杂度
	"""
	
	def helper_function(list_,start_pos,end_pos):
		if start_pos == end_pos:
			return list_[start_pos]
		mid_pos = start_pos + (end_pos - start_pos) / 2
		left_max = helper_function(list_,start_pos,mid_pos)
		right_max = helper_function(list_,mid_pos+1,end_pos)
		mid_max = 0
		t = 0
		for ind in range(start_pos,mid_pos):
			t += list_[ind]
			mid_max = max(mid_max,t)
		t = mid_max
		for ind in range(mid_pos,end_pos):
			t += list_[ind]	
			mid_max = max(mid_max,t)
		return max(left_max,mid_max,right_max)

	return helper_function(list_,0,len(list_)-1)
		

a = [4,-2,1,6,12,-8]
#print get_max_subarray_sum_by_dp(a)
print get_max_subarray_sum_by_dc(a)





































