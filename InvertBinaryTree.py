#!/usr/bin/env python2
#-*- coding:utf-8 -*-


# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
	
		if root is None:
			return root
		l = self.invertTree(root.left)
		r = self.invertTree(root.right)
		root.left,root.right = root.right,root.left
		return root	
				
       










 
