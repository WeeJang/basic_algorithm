#!/usr/bin/env python2
#-*- coding:utf-8 -*- 

"""麻将 判断手里的这个是否会和牌 
	满足 xABC + yAAA + DD
"""

import copy

def is_hu(pai_list):
	
	sorted_pai_list = sorted(pai_list)
	
	def meet_require(pai_counter):
		pai = []
		for e in pai_counter:
			pai.append(e)
			
							
	
	pai_counter = {}
	for e in sorted_pai_list:
		c = pai_counter.get(e,0)
		c += 1
		pai_counter[e] = c	
	#枚举DD
	#copy_counter
	for e in pai_counter:
		if pai_counter[e] > 1:
			copy_counter = copy.deepcopy(pai_counter)
			copy_counter[e] -= 2
			if meet_require(copy_counter):
				return True
	return False

		
