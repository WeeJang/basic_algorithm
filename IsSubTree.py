#!/usr/bin/env python2
#-*- coding:utf-8 -*-


class Node:
	
	def __init__(self,value):	
		self.value = value
		self.left,self.right = None,None

def is_sub_tree(large_tree,small_tree):
	""" 判断是否是子树 
		我当时用的是BFS搜索，其实没必要。直接递归就好。
	"""

	def is_same(large_tree,small_tree):
		""" 是否相同 """
		if large_tree is None and small_tree is None:
			return True
		if large_tree is None or small_tree is None:
			return False
		if large_tree.value != small_tree.value:
			return False
		return is_same(large_tree.left,samll_tree.left) and is_same(large_tree.right,small_tree.right)			

	if is_same(large_tree,small_tree):
		return True
	return is_sub_tree(large_tree.left,small_tree) or \
		is_sub_tree(large_tree.right,small_tree)


	
def is_sub_tree_2(large_tree,small_tree):
	"""
	这个通过字符串的方式。我当时想到了，但不敢确定 
	"""
	
	def seriable(tree,str_buffer):
		if tree is None:
			str_buffer.append("#")
			return
		seriable(tree.left)			
		seriable(tree.right)			
	
	large_tree_str_buffer = []
	seriable(large_tree,large_tree_str_buffer)	
	large_tree_str = ",".join(large_tree_str_buffer)	
	small_tree_str_buffer = []
	small_tree_str = ",".join(small_tree_str_buffer)	
	if large_tree_str.find(small_tree_str) == -1:
		return False
	return True

	
