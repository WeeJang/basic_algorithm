#!/usr/bin/env python
#-*- coding:utf-8 -*-

# get largest/smallest K-th num

import heapq

class LargestKth(object):
	
	def __init__(self,K,init_list):
		self.length = K	
		self.heap = init_list[:K]
		heapq.heapify(self.heap)
		for elem in init_list[K:]:
			self.put(elem)
	
	def put(self,new_elem):
		#连现任的Top-K中最小的一个都没超过，没资格进来评比
		if new_elem <= self.heap[0]:
			return
		else:
			self.heap[0] = new_elem #直接把Top-K中最小的替换
			heapq.heapify(self.heap)
	
	def peek(self):
		return self.heap[0]		
	

a = LargestKth(5,list(range(1,6)))	
for e in range(7,8):
	a.put(e)
	print a.peek()
	

	
		
