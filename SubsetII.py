#!/usr/bin/env python2
#-*- coding:utf-8 -*-


"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

借此延伸一下，如何对一个array of array 去重呢？
eg : 
  [ 
    [1,2,2],
    [2,2],
    [1,2]
    [2,2],
  ]

1)解法：
    将每一个元素转换成字符串，如上面那个就可以变成["1+2+2","2+2","1+2","2+2"],对字符串去重(set)
2)解法：
    构建一个Trie树，然后把Trie树读出来就可以了。

"""


"""
    DFS大法好！
"""

class Solution(object):
    
	def subsetsWithDup(self, nums):
		result = []
		if nums is None or len(nums) == 0:
			return result
		
		result.append([])
		#这一步排序很重要，保证了不会重复
		nums = sorted(nums)
		max_step = len(nums)

		def dfs_helper(start_i,max_len):
			""" 从result[start_i:]中取出不重复的array_set
			    len(array_set) == max_len 
			    :param start_i 开始索引
			    :param max_len 长度
			    :rtype [Boolean,[不重复的array_set]]
			"""
			#print "debug",start_i,max_len,"..."
			if start_i + max_len > len(nums):
				return False,None
			if start_i >= len(nums):
				return False,None
			if max_len == 1 :
				sets = set(nums[start_i:])
				#print "debug",start_i,max_len,True,[[e] for e in sets]
				#return True,[[e] for e in sets]
				#print "debug",start_i,max_len,True,[[nums[start_i]]]
				return True,[[e] for e in sets]

			ret_flag = False
			ret_array = []
			
			#choose nums[start_i]	
			last_value = None
			#相同的值跨过去，这样的话保证了不会有重复
			for i in range(start_i,len(nums)):
				if last_value is not None and last_value == nums[i]:
					continue
				is_ret,ret_list = dfs_helper(i+1,max_len -1)
				if not is_ret:
					continue
				ret_flag = True
				for l in ret_list:
					c = [nums[i]]
					c.extend(l)
					ret_array.append(c)
				last_value = nums[i]	

			#print "debug",start_i,max_len,ret_flag,ret_array
			return ret_flag,ret_array	
		
		for step in range(1,max_step+1):
			is_ret,ret_info = dfs_helper(0,step)
			if not is_ret:
				continue
			result.extend(ret_info)
		return result



# dfs(i,l) : choose all possible answer from nums[i:], where len(answer) == l
# dfs(i,l) 包含 dfs(i+1,l)





nums = [1,2,2,3]
solver = Solution()
print solver.subsetsWithDup(nums)

	





