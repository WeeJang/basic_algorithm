#!/usr/bin/env python2
#-*- coding:utf-8 -*-


"""
问题延伸自,如果nums里面存在重复元素

求子集问题(里面存在重复元素）


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



但是如果有重复元素呢？

我确实没想到，但看到leetcode上的分析，精妙！https://leetcode.com/problems/subsets-ii/discuss/30168
比如 例子中 [1,2,3] 其实当出现一个新元素3,新的子集相当于加这个元素产生的集合.
     也就是说全集是[1,2]的子集S1 + S1与3组合的子集S2
     也就是说全集是[1,2]'不添加3' 和 '添加3'两个状态后的子集和
对于 [1,2,3,3] 可以把(3,3) 当成一个special元素,
     那全集就是[1,2] '添加0个3','添加1个3','添加2个3' 这3个状态后的子集和

所以一上来得先排个序，比如说(1,2,2,3,3,..),每个元素对应的个数为k1,k2,k3  所以产生的子集个数为
(k1+1)*(k2+1)*(k3+1)

"""

import copy
class Solution(object):
    
	def subsetsWithDup(self, nums):
		result = []
		if nums is None or len(nums) == 0:
			return result
		nums = sorted(nums)
		nums.append("dummy") #dummy
		result.append([])
		last_value = None
		counter = 0
		for e in nums:
			if last_value is None:
				last_value = e
				counter = 1
				continue
			elif last_value is not None and last_value == e:
				counter += 1
				continue
			new_subset = copy.deepcopy(result)
			for i in range(counter):
				new_subset_copy = copy.deepcopy(new_subset)	
				for set_ in new_subset_copy:
					set_.extend([last_value]*(i+1))
				result.extend(new_subset_copy)
			last_value = e
			counter = 1
		return result

nums = [1,2,2,3]
solver = Solution()
print solver.subsetsWithDup(nums)
