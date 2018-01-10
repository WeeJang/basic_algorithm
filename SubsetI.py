#!/usr/bin/env python2
#-*- coding:utf-8 -*-


"""
求子集问题(里面没有重复元素）


Given a collection of integers that not contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2], a solution is:

[
  [2],
  [1],
  [1,2],
  []
]

解析：
对于没有重复元素的，直观想到的第一种方法：DFS。

但仔细思考一下，其实是排列组合问题，
假设有N个元素(1,2,..N)，则所有的subset可能情况
R = C(N,0) + C(N,1) + C(N,2) + .. C(N,N) 
C(N,i) 是长度为第i个元素加入后新增子集,R为结果集合list
C(N,0) = [[]]  (R[0:2^0])
C(N,1) = [[1]]  (R[2^0+1,2^1])
C(N,2) = [[2],[1,2]] (R[2^1+1,2^2])
...
C(N,N) = [...] (R[2^(N-1)+1,2^N])

len(R) = 2^N 

有没有发现，当第i个元素加入时，产生的新子集其实是组合了前面所有子集产生的。
因此可以迭代完成.
"""

import copy
class Solution(object):
    
	def subsetsWithNoDup(self, nums):
		result = []
		if nums is None or len(nums) == 0:
			return result
		result.append([])
		print result
		for e in nums:
			new_subset = copy.deepcopy(result)		
			for set_ in new_subset:
				set_.append(e)
			result.extend(new_subset)
		return result

nums = [1,2,3]
solver = Solution()
print solver.subsetsWithNoDup(nums)

	
















































