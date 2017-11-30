#!/usr/bin/env python2
#-*- coding:utf-8 -*-

import heapq


class TopKth(object):
	""" 第K大 """
	
	def __init__(self,K,init_list):
		self.K = K
		self.heap = init_list[:self.K]
		heapq.heapify(self.heap)
		for elem in init_list[self.K:]:
			self.put(elem)
	
	def put(self,new_elem):
		if len(self.heap) < self.K:
			self.heap.append(new_elem)
			heapq.heapify(self.heap)
		elif self.heap[0] < new_elem:
			self.heap[0] = new_elem
			heapq.heapify(self.heap)
		else:
			pass
	
	def peek(self):
		return self.heap[0]
	
	def remove(self,elem):
		if elem not in self.heap:
			return #TODO
		self.heap.remove(elem)
		heapq.heapify(self.heap)

	def debug(self):
		return self.heap


class LowKth(object):
	""" 第K小 """
	def __init__(self,K,init_list):
		self.K = K
		self.heap = [-elem for elem in init_list[:self.K]]
		heapq.heapify(self.heap)
		for elem in init_list[self.K:]:
			self.put(elem)
	
	
	def put(self,new_elem):
		new_elem *= -1
		if len(self.heap) < self.K:
			self.heap.append(new_elem)
			heapq.heapify(self.heap)
		elif self.heap[0] < new_elem:
			self.heap[0] = new_elem
			heapq.heapify(self.heap)

	def peek(self):
		return self.heap[0] * (-1)
	
	def debug(self):
		return self.heap

	def remove(self,elem):
		elem *= -1
		if elem not in self.heap:
			return #TODO
		self.heap.remove(elem)
		heapq.heapify(self.heap)

def SlidingWindowMidden(int_list,k):
	is_odd = True if k % 2 else False
	n = (k+1)/2 if is_odd else k/2
	top_k = TopKth(n,int_list[:k])
	low_k = LowKth(n,int_list[:k])
	
	def get_midden():
		top_k_num = top_k.peek()
		low_k_num = low_k.peek()
		middle_num = None
		if is_odd:
			middle_num = top_k_num
		else:
			middle_num = top_k_num * 0.5 + low_k_num * 0.5
		return middle_num,top_k_num,low_k_num
	
	print top_k.debug(),
	print low_k.debug(),
	mid_num,top_k_num,low_k_num = get_midden()
	#print mid_num,top_k_num,low_k_num
	print mid_num
	for i in range(1,len(int_list) - k + 1):
		print(int_list[i:i+k]),
		new_elem = int_list[i + k -1]
		old_elem = int_list[i - 1]
		top_k.remove(old_elem)
		low_k.remove(old_elem)
		
		#这一步很重要，先删掉窗口外的那个，然后补充对方那边的peek。	
		low_k_peek,top_k_peek = low_k.peek(),top_k.peek()	
		top_k.put(low_k_peek)
		low_k.put(top_k_peek)
		top_k.put(new_elem)
		low_k.put(new_elem)
		print top_k.debug(),
		print low_k.debug(),
		mid_num,top_k_num,low_k_num = get_midden()
		#print mid_num,top_k_num,low_k_num
		print mid_num


int_list = [1,3,-1,-3,5,3,6,7]
SlidingWindowMidden(int_list,4)		
