#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 最长回文子序列问题 

	DP : (1)最优子结构 (2)子问题重叠 
"""

def get_longest_hw_naive(str_,start_pos,end_pos):
	""" 这是采用朴素递归方法 
            重复求解子问题。
            复杂度 指数级
		( 1 + 2 + 4 + ..2^n-1 ) * C [一共n层，每层问题个数2^i]
        """
	if start_pos > end_pos :
		return 1
	if start_pos == end_pos:
		return 1
	if str_[start_pos] == str_[end_pos]:
		return 2 + get_longest_hw_naive(str_,start_pos+1,end_pos-1)	
	else:
		return max(get_longest_hw_naive(str_,start_pos,end_pos-1),get_longest_hw_naive(str_,start_pos+1,end_pos))


def get_longest_hw_DP_UB(str_):
	""" 采用DP方法,自上而下的带备忘录.
	    复杂度 O(n^2)
	"""
	def get_longest_hw(str_,start_pos,end_pos,lookup_table):
		if lookup_table[start_pos][end_pos] < float("inf"):
			return lookup_table[start_pos][end_pos]
		result = float("inf") 	
		if str_[start_pos] == str_[end_pos]:
			result = 2 + get_longest_hw(str_,start_pos+1,end_pos-1,lookup_table)
		else:
			result = max(get_longest_hw(str_,start_pos+1,end_pos,lookup_table),\
				   get_longest_hw(str_,start_pos,end_pos-1,lookup_table))
		lookup_table[i][j] = result
		return result
	#init table
	lookup_table = [ [ float("inf") for e in range(len(str_)) ] for e in range(len(str_))]	
	for i in range(len(lookup_table)):
		for j in range(len(lookup_table)):
			if i == j:
				lookup_table[i][j] = 1
			elif i > j:
				lookup_table[i][j] = 0
			else:
				pass
	#result
	return get_longest_hw(str_,0,len(str_)-1,lookup_table)	

def get_longest_hw_DP_BU(str_):
	"""自下而上求解
		复杂度 O(n^2)
	"""
	#M 中间结果 M[i][j] == str[i:j]的最长回文长度
	M = [[float("-inf") for i in range(len(str_))] for j in range(len(str_))]

	for i in range(len(str_)):
		M[i][i] = 1		
	for i in range(len(str_)):
		for j in range(0,i):
			M[i][j] = 0
	print M		
	for step in range(1,len(str_)):
		for i in range(len(str_)):
			j = i + step
			if j > len(str_) - 1:
				break	
			max_len = float("-inf")
			for m in range(0,j):
				cur_len = 0
				if str_[m] == str_[j]:
					cur_len = 2 + M[m+1][j-1]
				else:
					cur_len = M[m+1][j-1]
				if cur_len > max_len:
					max_len = cur_len
			M[i][j] = max_len

	print M		
	return M[0][len(str_)-1]	
			
	
c = "aemjhqiewza"
print get_longest_hw_naive(c,0,len(c)-1)
print get_longest_hw_DP_UB(c,)
print get_longest_hw_DP_BU(c,)



