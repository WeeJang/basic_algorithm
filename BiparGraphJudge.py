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
	print neighbor_dict
	#遍历Graph
	visited_node = set() #记录遍历过的节点
	def dfs(node):
		""" 从node节点出发，go
			如果当前节点未染色(-1),染成红色(0)
		    遍历周围节点，如果周围节点为未染色(-1)，染成与当前节点不同的颜色。
			如果当前节点已经染色，如果颜色一样，表明不能二分；否则可以继续
		"""
		print "visit...",node,color_dict
		if node in visited_node:
			return True
		visited_node.add(node)	#visit_node不能放在最后！！！
		if color_dict[node] == -1:
			color_dict[node] = 0
		for c_n in neighbor_dict[node]:
			print "fuck",c_n,color_dict[c_n]
			if color_dict[c_n] == -1:
				color_dict[c_n] = (color_dict[node] + 1) % 2 #0->1 1->0
			elif color_dict[c_n] == color_dict[node]:
				print node,c_n
				print color_dict
				return False
			else:
				pass
			if not dfs(c_n):
				return False
		print "end visit...",node
		return True
	
	for n in neighbor_dict.keys():
		if not dfs(n):
			return False
	return True


#N个学生
N = 10
elems = range(N)
#friends = [(1,2),(4,5),(1,5),(2,4)]
friends = [(1,2),(4,5),(1,5),(1,4)]

print is_bipar_graph(elems,friends)
	



