#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 是否是回文数 """

def is_palindrome(a):
	""" 121 yes ! 21 no!  no-use str space """
	max = a
	min = 0
	while max > 0:
		min = (min * 10 + max % 10)
		max /= 10
	return min == a


print is_palindrome(121)
print is_palindrome(21)		
	


























