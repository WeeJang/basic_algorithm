#!/user/bin/env python2
#-*- coding:utf-8 -*-

"""
http://blog.csdn.net/wwh578867817/article/details/44886709

应用：
1）类似hash表，check某个words是否出现在词典中
2) 输入提示：比如输入fuc后提示'k'

"""

END_FLAG = "DF_END"

class Trie(object):
	""" 前缀树／字典树／Trie树 """
	
	def __init__(self,words_set):
		self.trie = {}
		self.init_trie(words_set)

	def init_trie(self,str_set):
		for elem in str_set:
			self.add_elem_to_trie(elem)	
		print self.trie	
	
	def add_elem_to_trie(self,elem):
		p_t = self.trie
		for e in elem:
			p_e = p_t.get(e,{})
			p_t[e] = p_e
			p_t = p_e
		p_t[END_FLAG] = END_FLAG
	
	def find(self,elem):
		p_t = self.trie
		for e in elem:
			p_e = p_t.get(e)
			if p_e is None:
				return False
			p_t = p_e
		if END_FLAG in p_t:
			return True	
		return False	


a = ["abc","bce","cmf"]
tries = Trie(a)
print tries.find("ab")
print tries.find("abc")
















