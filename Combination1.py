#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" KS interview 
    返回Array的所有k个组合
    
    DFS搜索 比如[1,2,3,4,5]

    1 --> 2 --> 3 --> 4 --> 5
    |---------->|
    |---------------->|
    |---------------------->|
          |---------->|
          |---------------->|
                |---------->|
"""

def Combination(array,k):
	""" all combination """		
	
	def dfs(start_pos,K):
		""" 从start_pos开始，取K个 """
		if start_pos + K - 1 >= len(array):
			return None		
		if start_pos >= len(array):
			return None
		if K == 1:
			return [ [e] for e in array[start_pos:] ]
		
		res = []
		for i in range(start_pos + 1,len(array)):
			dfs_r = dfs(i,K-1)
			if dfs_r is None:
				continue
			for r in dfs_r:
				if r == None:
					continue
				c = [ array[i-1] ]
				c.extend(r)
				res.append(c)
		if len(res) == 0:
			return None
		return res
	
	r = dfs(0,k)
	if r is None:
		return []
	return r

array = ["a","b","c","d","e","f"]
print Combination(array,100)			
