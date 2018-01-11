#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
 Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

 obj:{
	abs(nums[i] - nums[j]) <= t  (1)
	abs(i - j) <= k              (2)
     }

# 思路:bucket-sort

# 其实遇到gap相关的，可以考虑一下桶的想法

# bucket_width : t + 1
# 假设存在i,j满足条件
# 则两种情况：
#   1） i,j 在同一个桶中；
#   2） i,j 在不同的桶中;
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
	if t < 0:
		return False
	if nums is None or len(nums) == 0:
		return False
	bucket = {} #bucket中仅记录k个元素,来保证满足条件(2)
	bucket_width = t + 1 
	
	for i in range(len(nums)):
		bucket_id = nums[i] / bucket_width
		if bucket_id in bucket:
			return True
		elif bucket_id - 1 in bucket and abs(nums[i] - bucket[bucket_id-1]) <= t:
			return True
		elif bucket_id + 1 in bucket and abs(nums[i] - bucket[bucket_id+1]) <= t:
			return True
		bucket[bucket_id] = nums[i]
		if i >= k:
			del(bucket[nums[i-k]/bucket_width])
	return False	




nums = [-1,-1]
k = 1
t = -1

solver = Solution()

res = solver.containsNearbyAlmostDuplicate(nums,k,t)
print res




