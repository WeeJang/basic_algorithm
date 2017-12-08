#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" Union of Array """

"""
1)sort two array
2)binary find (不用，直接两个指针走就行)
"""



def find_union_of_two_array(list_1,list_2):

	if list_1 == None or list_2 == None:
		return []
	len_a,len_b = len(list_1),len(list_2)
	if len_a * len_b == 0:
		return []
	A,B = sorted(list_1),sorted(list_2)
	union_set = set()
	
	p_a,p_b = 0,0
	while True:
		if A[p_a] == B[p_b]:
			union_set.add(A[p_a])
			p_b += 1
			p_a += 1
		elif A[p_a] > B[p_b]:
			p_b += 1
		else:
			p_a += 1
		
		if p_a >= len_a or p_b >= len_b:
			break
	return list(union_set)		
