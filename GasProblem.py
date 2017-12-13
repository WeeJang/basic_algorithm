#!/usr/bin/env python2
#-*- coding:utf-8 -*-



def can_circulate(gas,cost):

	# can ? diff -> sum(diff) > 0 
	if sum(gas) - sum(cost) < 0:
		return -1
	# find where
	# Greedy-Algorithm :
	#               > 0
	diff = [ 0 for i in range(len(gas)) ]
	for i in range(len(gas)):
		diff[i] = gas[i] - cost[i]
	i,start = 0,None
	accum = 0
	while True:
		if start == i:
			break
		if accum + diff[i] < 0: 
			start = None
			accum = 0
		else: # >= 0:
			if start is None:
				start = i
			accum += diff[i]
		i += 1
		i = i % len(diff)
	return start		


gas=[1, 1, 3, 1]
cost=[2, 2, 1, 1]

s = can_circulate(gas,cost)
print(s)






