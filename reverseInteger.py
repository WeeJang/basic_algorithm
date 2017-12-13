#!/usr/bin/env python2
#-*- coding:utf-8 -*-


def reverse_integer(a):
	flag = 1
	if a < 0:
		flag = -1
	a = abs(a)
	r = 0
	while True:
		if flag == 1 and r > 2**31 - 1:
			return 0
		if flag == -1 and r > 2**31:
			return 0
		r = r * 10 + (a % 10)
		a = a / 10
		if a == 0:
			break
	return flag * r

print reverse_integer(128)
print reverse_integer(-128)
			
