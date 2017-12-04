#!/usr/bin/env python2
#-*- coding:utf-8 -*- 

from itertools import izip_longest,islice

"""
	Suffix Array : Processing String 

	RawString = "..."
	Suffix[i] = RawString[i:]
	SA[i]   #后缀数组:将所有后缀排序后，依此将这些后缀数组的第一个位置放在SA在。也就是排名第i个的suffix在位于RawString的第SA[i]个位置
	Rank[i] #排名数组:保存Suffix[i]的名次
	Suffix[SA[i]] <= Suffix[SA[i+1]]
"""

class SuffixArray(object):

	def __init__(self,raw_string):
		self.raw_string = raw_string
		self.SA = []
		self.Rank = []
		self.create_suffix_array()

	def elem_to_int(self,elem_list):
		""" """
		elem_set = set()
		for elem in elem_list:
			elem_set.add(elem)
		unique_elem_list = list(elem_set)
		unique_elem_list.sort()
		print("---->",unique_elem_list)
		elem_dict = { e:i for i,e in enumerate(unique_elem_list) }
		int_list = [ elem_dict[e] for e in elem_list ]
		return int_list	

	def reverse_array(self,array):
		r_array = [0] * len(array)
		for i,e in enumerate(array):
			r_array[e] = i
		return r_array
	
	def create_suffix_array(self):
		""" 2 fold inc
		      - N进制的基底
		"""
		k = 1
		elem = list(self.raw_string)
		N = len(elem)
		int_elem = self.elem_to_int(elem)
		while max(int_elem) < N - 1:  #在没确定顺序前，int_elem中存在重复元素的，即max(int_elem) < N-1,这个看OIpaper图可以看出
			elem = [ a * N + (b+1) \
				for a,b in \
					izip_longest(int_elem,islice(int_elem,k,None),fillvalue = -1) ]
			int_elem = self.elem_to_int(elem)
			#print list(int_elem)
			k <<= 1
		#print list(int_elem)
		self.Rank = int_elem
		self.SA = self.reverse_array(self.Rank)

	def debug(self):
		print "{{{ suffix_array ..."
		for elem in self.SA:
			print self.raw_string[elem:]	
		print "... suffix_array }}}"

sa = SuffixArray("helloallen")
#print(sa)
sa.debug()


