#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.



Presum + HashMap
"""

class Solution(object):

	def subarraySum(self, nums, k):
        	"""
       	 	:type nums: List[int]
        	:type k: int
        	:rtype: int
        	"""
		if nums is  None:
			return 0
		pre_sum = 0
		pre_sum_dict = {0:1}
		accum = 0
		for i in range(len(nums)):
			pre_sum += nums[i] #a ,and a - b = k
			b = pre_sum - k
			accum += pre_sum_dict.get(b,0)
			num_a = pre_sum_dict.get(pre_sum,0)
			pre_sum_dict[pre_sum] = (num_a + 1)
		return accum

nums = [1,1,1]
k = 2	

#nums = [1,2,3]
#k = 3
#nums = [1]
#k = 0
#nums = [-1,-1,1]
#k = 1

solver = Solution()
print solver.subarraySum(nums,k)
