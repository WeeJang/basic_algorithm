#!/usr/bin/env python2
#-*- coding:utf-8 -*-


""" 0-1 背包问题 
    KW-Interview :
	出了一个变形。就是每个房间有观众，观众有一定的粉丝。
"""




def ZeroOneBag(weights,values,max_load):
	""" transfer function 
	param:
		weights:list[float]
		values :list[float]
		max_weight:float
	return:
		max_value:float
	"""
	#BF + NoteBook
	note_book = {} # start->{left_space->opt_tuple}
	def dfs(start_pos,left_space):
		"""
		从object[start_pos:],剩余空间left_space选出的最优结果 
		rtype:
			max_v:float max value
			max_l:list[index] indexs of max_value
		"""
		try_find = note_book.get(start_pos,{}).get(left_space)
		if try_find != None:
			return try_find
		max_v,max_l = 0,[]
		if start_pos == len(weights):
			return max_v,max_l
		if left_space == 0:
			return max_v,max_l
		for i in range(start_pos+1,len(weights)):
			if weights[i] > left_space:
				continue
			c_max_v,c_max_l = dfs(i,left_space - weights[i])
			if c_max_v + values[i] > max_v:
				max_v = c_max_v + values[i]
				max_l = [i]
				max_l.extend(c_max_l)
		pos_map = note_book.get(start_pos,{})
		note_book[start_pos] = pos_map
		pos_map[left_space] = (max_v,max_l)
		return max_v,max_l
	return dfs(0,max_load)	

weights = [10,20,30,40]
values = [20,30,40,60]
max_load = 80
print ZeroOneBag(weights,values,max_load)

