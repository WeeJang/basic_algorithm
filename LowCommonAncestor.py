#!/usr/bin/env python2
#-*- coding:utf-8 -*-


class Node(object):
	
	def __init__(self,value):
		self.value = value
		self.left,self.right = None,None


def get_low_common_ancestor(root,value_1,value_2):
	""" 这里需要利用二叉树的搜索性质 
	
		left < root < right
	"""
	
	if root is None:
		return None
	min_value,max_value = min(value_1,value_2),max(value_1,value_2)
	if min_value <= root and root <= max_value:
		return root
	if min_value < root and max_value < root:
		return get_low_common_ancestor(root.left,value_1,value_2)
	if min_value > root and max_value > root:
		return get_low_common_ancestor(root.right,value_1,value_2)
			
		
			
	
	
								





