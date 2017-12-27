#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""N个学生,m对相互认识，问能否分成两组，让组内的人都互相不认识 """

#N个学生
N = 10
elems = range(N)
friends = [(1,2),(4,5),(1,5),(2,4)]
#friends = [(1,2),(4,5),(1,5),(1,4)]

def is_bipar_graph(elems,friends):
	""" 二分图 判定(至少有两点，且所有回路的必须是偶数,不存在奇环
	      染色法 
	"""
	#结点染色字典 -1 未染色，0 red 1 black
	color_dict = {}
	for i in elems:
		color_dict[i] = -1
	
	#构建邻接表 { "node" -> "neighbor_set" }
	neighbor_dict = {}
	for i in elems:
		neighbor_dict[i] = set()
	for cp in friends:
		neighbor_dict[cp[0]].add(cp[1])
		neighbor_dict[cp[1]].add(cp[0])
	#遍历Graph
	def dfs(node):
					
			
	
	
















