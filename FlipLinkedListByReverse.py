#!/usr/bin/env python2
#-*- coding:utf-8 -*-


class Node(object):
	
	def __init__(self,value):
		self.value = value
		self.next_ = None


def create_linked_list_from_list(list_):
	head_node = None
	p_node = None	
	for elem in list_:
		new_node = Node(elem)
		if head_node is None:
			head_node = new_node
			p_node = head_node
		else:
			p_node.next_ = new_node
			p_node = new_node
	return head_node


def print_linked_list(node):
	while node is not None:
		print node.value,"==>",
		node = node.next_


# flip linked list
def flip_linked_list_by_reverse(node):
	""" 返回反转后的头节点	这样写简洁，但是复杂度高"""

	if node.next_ == None:
		return node
	filped_next = flip_linked_list_by_reverse(node.next_)
	node.next_ = None
	p_node = filped_next
	while p_node.next_:
		p_node = p_node.next_
	p_node.next_ = node	
	return filped_next
		
	


head_node = create_linked_list_from_list([1,2,3,4,5])
print_linked_list(head_node)
print "===="		
r_list = flip_linked_list_by_reverse(head_node)
print_linked_list(r_list)
