#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 单词接龙问题 """

""" 特点:全部小写，长度还一样。其实可以遍历（字母表）获得dis=1的东西 """

def ladderLength(start, end, words_set):
	""" 每次更改一个charactor """


	def is_near(str_1,str_2):
		counter = 0
		for i in range(len(str_1)):
			if str_1[i] != str_2[i]:
				counter += 1
		return counter == 1	

	def find_near_list(words_set):
		near_dict = {}
		for i in range(len(words_set)):
			for j in range(i,len(words_set)):
				if is_near(words_set[i],words_set[j]):
					l = near_dict.get(words_set[i],[])
					l.append(words_set[j])
					near_dict[words_set[i]] = l
					l = near_dict.get(words_set[j],[])
					l.append(words_set[i])
					near_dict[words_set[j]] = l
		return near_dict
	
	words_set.append(start)	
	words_set.append(end)	
	near_dict = find_near_list(words_set)
	
	def find_path(seen_set,candidate_list,target):
		print "seen_set",seen_set
		if candidate_list is None:
			return None
		if target in candidate_list:
			return [[]] #无比保证返回结果的一致性
		ret_list = []
		for elem in candidate_list:
			if elem in seen_set:
				continue
			s = set(seen_set)
			s.add(elem)
			path_list = find_path(s,near_dict.get(elem),target)
			if path_list is None:
				continue				
			else:
				for p in path_list:
					r = [elem]
					r.extend(p)
					ret_list.append(r)
		return ret_list	 
	print near_dict
	all_path = find_path(set(),near_dict.get(start),end)
	shortest_path = None
	shortest_path_len = float('inf')
	for p in all_path:
		if len(p) < shortest_path_len:
			shortest_path = p
	return shortest_path	
	
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
print ladderLength(start,end,dict)
