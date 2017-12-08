#!/usr/bin/env python2
#-*- coding:utf-8 -*-


class Node(object):
	
	def __init__(self,value):
		self.value = value
		self.right,self.left = None,None

""" pre-order to fake list """

def flatten_binary_tree(tree):

	def pre_order_travel(tree,node_buffer):
		if tree is None:
			return
		node_buffer.append(tree.value)
		pre_order_travel(tree.left,node_buffer)
		pre_order_travel(tree.right,node_buffer)
	
	node_buffer = []
	pre_order_travel(tree,node_buffer)
	root = None
	if len(node_buffer) == 0:
		return root
	root = Node(node_buffer[0])
	p_node = root
	for elem in node_buffer[1:]:
		new_node = Node(elem)
		p_node.right = new_node
		p_node = new_node
	return root	



def flatten_binary_tree_by_recursion(tree):
	""" 用递归的方式,先考虑的就是这种方式 """

	def recursion_helper(tree):
		""" 返回头节点和尾节点 """
		
		if tree.right == None and tree.left == None:
			return tree,tree
		
		left_flat = recursion_helper(tree.left)
		right_flat = recursion_helper(tree.right)
		
		tree.right = left_flat[0]
		left_flat[1].right = right_flat[0]
		return tree,right_flat[1]	
	
	tree_node,_ = recursion_helper(tree)	
	return tree_node

