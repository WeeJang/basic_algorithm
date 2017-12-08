#!/usr/bin/env python2
#-*- coding:utf-8 -*- 


""" Yang Tableue """

import heapq


class Elem(object):
		
	def __init__(self,value,cord):
		self.value = value
		self.cord = cord

	def __cmp__(self,other):
		if self.value < other.value:
			return -1
		elif self.value == other.value:
			return 0
		else:
			return 1	


def get_K_th_in_Yang(yang_matrix,K):
	""" 结构类似heap。刚开始思考的时候，在如何搜索上卡住了。
		看到BFS恍然大悟，跟2-d接雨水有的一拼。非常精彩。
		要好好理解 BFS，并非只是知道"""
	
	row_len,col_len = len(yang_matrix),len(yang_matrix[0])
	
	def get_elems_from_list_by_BFS(cord):
		elem_list = []
		if cord[0] == row_len - 1 and cord[1] == col_len - 1:
			return []
		if cord[0] == row_len - 1:
			return [Elem(yang_matrix[cord[0]][cord[1]+1],cord[0],cord[1]+1),]				
		if cord[1] == col_len - 1:
			return [Elem(yang_matrix[cord[0]+1][cord[1]],cord[0]+1,cord[0]),]				
		else:
			return [Elem(yang_matrix[cord[0]][cord[1]+1],cord[0],cord[1]+1),
				Elem(yang_matrix[cord[0]+1][cord[1]],cord[0]+1,cord[0]),]				
	
	heap = []
	
	k_th = -1
	k_counter = 0

	heap.append(Elem(yang_matrix[0][0],(0,0)))
	
	while k_counter < K:
		heapq.heapify(heap)
		top_elem = heap.pop(0)
		k_th = top_elem.value
		cord = top_elem.value	
		#BFS 
		elems = get_elems_from_list_by_BFS(cord)
		heap.extends(elems)	
		k_counter += 1
	return k_th









											




