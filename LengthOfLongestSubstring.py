#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" lengthOfLongestSubstring 最长无重复子串 
    思考"后缀数组"解法
"""

def lengthOfLongestSubstring(s):
	
	""" lengthOfLongestSubstring """
	counter = {}
	i,j = 0,-1
	
	max_len = 0
	max_i = -1
	#invariant: s[i:j] is no-repeat string
	while j < len(s) - 1:
		j += 1
		if s[j] not in counter:
			counter[s[j]] = 1
			continue

		if counter[s[j]] == 0:
			counter[s[j]] = 1
		else:
			if j-i > max_len:
				max_len = j-i
				max_i = i
			# move i
			while s[i] != s[j] and i <= j:
				i += 1
				counter[s[i]] -= 1
			i += 1
	#print "i {} j {} max_len {}".format(i,j,max_len)
	if j-i > max_len:
		max_len = j-i
		max_i = i

	return max_i,max_len

print lengthOfLongestSubstring("abcabaemgqfc")	
