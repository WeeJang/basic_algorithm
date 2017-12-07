#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 循环不变式"""

def is_odd(elem):
	if elem % 2 == 0:
		return True
	else:
		return False


def re_range_odd(list_):
	""" re-range-odd """
	#[0,bound] is odd
	bound = -1
	
	for ind in range(len(list_)):
		if is_odd(list_[ind]):
			bound += 1
			list_[bound],list_[ind] = list_[ind],list_[bound]
	

a = list(range(10))
re_range_odd(a)
print(a)						
