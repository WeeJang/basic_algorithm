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
def flip_linked_list(node):
	
	if node == None:
		return None
	
	p_a,p_b = None,None
	temp = None
	while True: #如果不确定跳出条件就这样写
		if p_a == None and p_b == None:
			p_a,p_b = node,node.next_
			p_a.next_ = None #先制造循环不变式子
		temp = p_b.next_
		p_b.next_ = p_a
		p_a = p_b
		p_b = temp
		if p_b == None:
			break
	return p_a
	


head_node = create_linked_list_from_list([1,2,3,4,5])
print_linked_list(head_node)
print "===="		
r_list = flip_linked_list(head_node)
print_linked_list(r_list)
