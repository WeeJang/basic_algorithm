#!/usr/bin/env python2
#-*- coding:utf-8 -*-


"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

"""

"""
其实这个问题考察的是 前／中／后序遍历的使用场景。
前序：先访问该节点，然后再访问左子树和右子树。
中序：先访问左子树，该节点，右子树。对于BST来说，这样可以输出有序的结果
后序：先访问左右子树，再访问该节点。
"""




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
	
	def poster_order(root,tree_str_dict,same_tree_list):
		"""
		:param
			root : 根节点 type:TreeNode
			tree_str_dict : 已经遍历过的树 及其个数 type:dict<str,int>
			same_tree_list: 相同的树 type:List[TreeNode]
		:return
			树的后序结果
		"""
		if root is None:
			return "#"
		tree_str = "%s,%s,%s" % (poster_order(root.left,tree_str_dict,same_tree_list)\
					,poster_order(root.right,tree_str_dict,same_tree_list),root.val)
		num =  tree_str_dict.get(tree_str,0)
		if num == 1:
			same_tree_list.append(root)
		num += 1
		tree_str_dict[tree_str] = num
		return tree_str
	res = []
	tree_dict = {}
	poster_order(root,tree_dict,res)
	return res	
			










        
