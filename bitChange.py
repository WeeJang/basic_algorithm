#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 比特修改 """

def bit_change_err(a,b):
	""" 这个解法是错误的，负数不成立"""
	bit_counter = 0
	c = a ^ b
	
	while c != 0:
		bit_counter += (c % 2)
		c = c >> 1
	return bit_counter


def bit_change(a,b):
	bit_counter = 0
	c = a ^ b

	flag = 1
	while True:
		if c & flag > 0:
			bit_counter += 1 	
		flag = (flag<< 1)
		if flag > (1<<31):
			break
	
	return bit_counter


print bit_change(31,14)
print bit_change(1,-1)
	




























