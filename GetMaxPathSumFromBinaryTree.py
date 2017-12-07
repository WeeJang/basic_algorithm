#!/usr/bin/env python2 
#-*- coding:utf-8 -*- 

""" 返回二叉树最大路径的和 """

class Node(object):

	def __init__(self,value):
		self.value = value
		self.left,self.right = None,None


""" DP 解决"""
def get_max_path_sum(tree):

	
	def cal_tree(tree):
		""" 返回当前tee的最大路径和，和最大深度
			(max_path_sum,max_deepth)
		"""
		if tree is None:
			return (0,0)
		left_r,right_r = cal_tree(tree.left),cal_tree(tree.right)
		max_deepth = max(left_r[1],right_r[1]) + 1
		max_path_sum = max(left_r[1] + right_r[1] + 1,left_r[0],right_r[0])
		return (max_path_sum,max_deepth)
	res = cal_tree(tree)
	return res[0]



	
	
	
	

