#!/usr/bin/env python2
#-*- coding:utf-8 -*-


class Node(object):
	def __init__(self,value):
		self.value = value
		self.left,self.right = None,None


#保证用同一种方式。这里我们采用前序(根->左->右),中序(左->根->右)
class Solution(object):

	def serialize(self,root):
		str_buffer = []
		def serialize_tree(root,str_buffer):
			if root is None:
				str_buffer.append("#")
			else:
				str_buffer.append(root.value)
				serialize_tree(root.left,str_buffer)			
				serialize_tree(root.right,str_buffer)			
		serialize_tree(root,str_buffer)
		return "{" + ",".join(str_buffer) + "}"
	
	
	def deseriable(self,data):
		elem_list = data[1:-1].split(",")
		
		def deseriable_tree(data_list):
			if len(data_list) == 0:
				return None
			elem = data_list.pop(0)
			if elem == "#":
				return None
			else:
				root = Node(elem)
				root.left  = deseriable_tree(data_list)
				root.right = deseriable_tree(data_list)
				return root
		return deseriable_tree(elem_list)	
				
				
		


test_case = "{3,9,20,#,#,15,7}"

solution = Solution()

tree = solution.deseriable(test_case)
print(tree)
output_str = solution.serialize(tree)
print(output_str)



