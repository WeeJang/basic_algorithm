#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" merge two sorted array """

def merge_sorted_array(array_a,array_b):
	
	i,j = 0,0
	ret = []
	while i < len(array_a) and j < len(array_b):
		if array_a[i] < array_b[j]:
			ret.append(array_a[i])
			i += 1
		else:
			ret.append(array_b[j])
			j += 1
	if i >= len(array_a):
		ret.extend(array_b[j:])
	if j >= len(array_b):
		ret.extend(array_a[i:])
	return ret

A=[1,2,3,4]
B=[2,4,5,6]
print merge_sorted_array(A,B)


