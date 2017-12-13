#!/usr/bin/env python2
#-*- coding:utf-8 -*-


""" Major Member  beyond n/2 """

def get_major_member(nums):
	"""低消法"""
	candidate,counter = 0,0
	for elem in nums:
		if counter == 0:
			candidate = elem
			counter += 1
			continue
		if elem == candidate:
			counter += 1
		else:	
			counter -= 1
	return candidate

a = [1,1,2]
print get_major_member(a)	




























