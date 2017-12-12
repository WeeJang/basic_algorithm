#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 返回可构成的最大数 """
# "8","843","89","81","65"

""" 前缀问题？
要满足的效果如下:

"89" > "843"
"89" > "897"
"89" < "899" [从这两个栗子可以看出要补8]
"8" > "843"
"8" < "89"
"""

class Elem(object):
	def __init__(self,v):
		self.v = str(v)
	
	def __cmp__(self,other):
		if self.v + other.v > other.v + self.v:
			return 1
		elif self.v + other.v < other.v + self.v:
			return -1
		else:
			return 0
 
def get_max_integer(num_list):
	ret_str = ""
	e_list = [Elem(e) for e in num_list]
	print([e.v for e in e_list])
	sorted_list = sorted(e_list,reverse = True)
	print([e.v for e in sorted_list])
	str_list = [e.v for e in sorted_list]
	return "".join(str_list)

a = [89,4,897,89,843,4]
print get_max_integer(a)
								
		






