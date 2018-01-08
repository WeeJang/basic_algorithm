#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
Bag problem i:

Given n items with size Ai, an integer m denotes the size of a backpack.
How full you can fill this backpack?

[reference]http://www.ahathinking.com/archives/95.html
"""

def max_weights(weights,upper):
	"""
	W(i,upper) : the max_weight of weights[:i] in upper
	obj[i] choose or not
	
	W(i,upper) = max( W(i-1,upper),\  #not choose
			  W(i-1,upper-weights[i]) + weights[i] if upper<=weights[i] #choose
			) for i in (0,...,len(obj))

	#NOTE : general is W(i,upper) = max( W(i-1,upper),\ #not choose
				             W(i-1,upper-weight[i]) + value[i] if upper <= weight[i] # choose
					   )
	"""
	
	W = [ [ u for u in range(upper+1) ] for i in range(len(weights)) ]
	
	for i in range(len(weights)):
		for j in range(upper+1):
			if i == 0:
				if j < weights[i]:
					W[i][j] = 0
				else:
					W[i][j] = weights[i]
			else:
				W[i][j] = W[i-1][j]
				if j >= weights[i]:
					tmp = W[i-1][j-weights[i]] + weights[i]
					if tmp > W[i][j]:
						W[i][j] = tmp
	print W
	return W[len(weights)-1][upper]




#weights = [2,3,5,7]
weights = [2,6,5,7]
upper = 11
print max_weights(weights,upper)
