#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" Anagrams 
    有没有一种哈希算法（不考虑传入的元素的顺序？）
    脑洞.
"""

def anagrams(str_list):

	def resort_string(elem):
		if elem is None:
			return None
		return "".join(sorted(elem))	
	res = []
	counter = {}
	for ind,elem in enumerate(str_list):
		re_elem = resort_string(elem)
		if re_elem not in counter:
			counter[re_elem] = ind
		else:
			if counter[re_elem] >= 0:
				res.append(str_list[counter[re_elem]])
				counter[re_elem] = -1 #标记参照字符串已经放入res
			res.append(elem)
	return res	

a = ["ab","bc","ba"]
print anagrams(a)
