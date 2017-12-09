#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" Add Two Numbers II : 栈"""

class ListNode:
	def __init__(self,val):
		self.val = val
		self.next = None		

def trans_to_stack(l):
	stack = []
	for elem in l:
		stack.append(elem)
	return stack
	
def add_two_numbers(l1,l2):
	stack_1 = trans_to_stack(l1)	
	stack_2 = trans_to_stack(l2)
	p_node = None
	promote = 0
	while len(stack_1) > 0 or len(stack_2) > 0:
		a , b = 0,0
		if len(stack_1) > 0:
			a = stack_1.pop()
		if len(stack_2) > 0:
			b = stack_2.pop()
		c = a + b + promote
		promote = c % 10
		c = c / 10
		new_n = ListNode(c)
		if p_node is None:
			p_node = new_n
		else:
			new_n.next = p_node
			p_node = new_n
	return p_node






