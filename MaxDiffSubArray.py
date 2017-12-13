#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 最大不同的子数组A,B 使得|sum(A) - sum(B)|最大 """

def max_diff_sub_array(nums):
	""" """

	def find_max_clique(nums):
		""" DP L[i]以第i个为尾部的数组最大值 """
		L = [ 0 for i in range(len(nums)) ]
		for i in range(len(nums)):
			if i == 0:
				L[i] = nums[i]
			else:
				L[i] = max(L[i-1]+nums[i],nums[i])								
		return max(L)
	
	def find_min_clique(nums):
		""" DP same """
		L = [ 0 for i in range(len(nums)) ]
		for i in range(len(nums)):
			if i == 0:
				L[i] = nums[i]
			else:
				L[i] = min(L[i-1]+nums[i],nums[i])
		return min(L)
	
	return find_max_clique(nums) - find_min_clique(nums)

a = [1, 2, -3, 1]
print max_diff_sub_array(a)

