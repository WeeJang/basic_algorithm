#!/usr/bin/env python2
#-*- coding:utf-8 -*-


class Node:
	def __init__(self,value):
		self.value = value
		self.left,self.right = None,None


def insert_elem_into_BST(bst,value):

	def helper(c_bst,value):
		if c_bst.value > value:
			if c_bst.left == None:
				c_bst.left == Node(value)
			else:
				helper(c_bst.left,value)
		else:
			if c_bst.right == None:
				c_bst.right == Node(value)
			else:
				helper(c_bst.right,value)

	helper(bst,value)
