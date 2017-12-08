#!/usr/bin/env python2
#-*- coding:utf -*-

"""
给定一个字符串source和一个目标字符串target，在字符串source中找到包括所有目标字符串字母的子串。
 注意事项
如果在source中没有这样的子串，返回""，如果有多个这样的子串，返回起始位置最小的子串。
"""

"""
问题分析
 1.元素均为字符串，且不用考虑顺序
 2.构建target字串的hashmap
"""
def find_min_sub_string_corver(source,target):
	
	"""将target 构建计数字典 ,然后利用两个指针 
		总体复杂度 O(len(source)) * 2 * O(26) = O(N)
	"""

	if len(target) * len(source) == 0:
		return -1
	p_s,p_e = 0,0
	len_s = len(source)
	
	# 字符串被覆盖时，counter中所有value <= 0
	counter = {}	
	for elem in target:
		c = counter.get(elem,0)	
		c += 1
		counter[elem] = c

	def is_corvered():
		""" 这个操作的时间复杂度O(26) """
		for k in counter:
			if counter[k] > 0:
				return False
		return True

	def add_elem(elem):
		if elem in counter:
			counter[elem] = counter[elem] + 1
	
	def reduce_elem(elem):
		if elem in counter:
			counter[elem] = counter[elem] - 1

	result_buffer = []		
	while True:
		s_flag,e_flag = False,False
		while p_e < len_s:
			elem = source[p_e]
			reduce_elem(elem)
			p_e += 1	
			if is_corvered(): #覆盖了
				e_flag = True
				break
		while p_s < p_e:
			elem = source[p_s]
			add_elem(elem)
			p_s += 1
			if not is_corvered(): #失去覆盖
				s_flag = True
				break
		if s_flag and e_flag:	
			result_buffer.append((p_s-1,p_e))
		if p_e == len_s:
			break
	return result_buffer
					
source_str = "ADOBECODEBANC"
target_str = "ABC"	
result =  find_min_sub_string_corver(source_str,target_str)
print result
for elem in result:
	print elem
	print source_str[elem[0]:elem[1]]
