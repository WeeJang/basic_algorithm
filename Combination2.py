#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 数组所有的可能排列组合

如[1,1,2]
=>
[ [1,1,2],
  [1,2,1],
  [2,1,1]]
"""
import copy

def AllCombination(array):
	""" """
	def dfs(elems):
		""" 返回elems的全排列 
		param : list[int]
		return : list[list[int]]
		"""
		if len(elems) == 1:
			return [elems]
		res = []
		visited = set()
		for i in range(len(elems)):
			if elems[i] in visited:
				continue
			copy_elems = copy.copy(elems)
			e = copy_elems.pop(i)
			for left_c in dfs(copy_elems):
				new_c = [e]
				new_c.extend(left_c)
				res.append(new_c)
			visited.add(e)
		return res
	return dfs(array)	
			
array = [1,1,2]
print AllCombination(array)























