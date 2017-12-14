#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" KMP算法 
	[1] https://www.zhihu.com/question/21923021
	但是上面的思考中有一点得明确，其实自己的思考的是“乙“,也就是模式P。
	（AC-aumtion是多模式的KMP)
	[2] http://blog.csdn.net/yutianzuijin/article/details/11954939/
	3 next_array 是最长后缀的匹配的最长前缀
	
"""

def KMP(pattern,string):
	""" KMP string match """
	def pre_process(pattern):
		""" 失配函数 预处理 next 
		next[i] : 代表当pattern[i] 与 string[i]失配后，再pattern[next[i]]与string[i]进行比较
			  -1 代表回溯结束，乖乖从0新开始(pattern[0])
		""" 
		next_array = [ -1 for i in range(len(pattern)) ]
		for i in range(1,len(pattern)):
			j = next_array[i-1]
			#寻找pattern[:i]的后缀中能与自己匹配到最长前缀的那个
			while j != -1 and pattern[i-1] != pattern[j]:
				j = next_array[j]
			if pattern[i-1] == pattern[j]: #第pattern[i-1]与pattern[j]配上了
				next_array[i] = j + 1
			else:
				next_array[i] = -1
		return next_array 	
	
	def is_match(string,pattern):
		next_array = pre_process(pattern)
		p_s,p_p = 0,-1 #p_p = -1 means re-start
		while True:
			if string[p_s] == pattern[p_p] or p_p == -1:
				p_s += 1
				p_p += 1
			else:
				p_p = next_array[p_p]
			if p_p > len(pattern) - 1:
				return True
			if p_s > len(string) - 1:
				return False
	return is_match(string,pattern)

pattern = "abab"
string = "cababc"
print KMP(pattern,string)
