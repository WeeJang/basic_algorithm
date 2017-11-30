#!/usr/bin/env python2
#-*- coding:utf-8 -*-


class Node(object):
	def __init__(self,value):
		self.value = value
		self.left,self.right = None,None


#采用层序遍历(BFS)

class Solution(object):

	def serialize(self,root):
		queue = []
		queue.append(root)
		str_buffer = []
		while len(queue) != 0:
			node = queue.pop(0)
			if node is None:
				str_buffer.append("#")
			else:
				str_buffer.append(node.value)
				queue.append(node.left)
				queue.append(node.right)
		return "{" + ",".join(str_buffer) + "}"		
	
	def deseriable(self,data):
		elem_list = data[1:-1].split(",")
		root = None
		if elem_list[0] == "#":
			return root
		else:
			root = Node(elem_list[0])
		queue = [root]
		head_color = 0 # 0:none 1:left 							
		for elem in elem_list[1:]:
			node = None
			if elem != "#":
				node = Node(elem)
				queue.append(node)
			if head_color == 0:
				queue[0].left = node
				head_color = 1
			else:
				queue[0].right = node
				queue.pop(0)
				head_color = 0
		return root 
			
		

test_case = "{3,9,20,#,#,15,7}"

solution = Solution()

tree = solution.deseriable(test_case)
print(tree)
output_str = solution.serialize(tree)
print(output_str)



