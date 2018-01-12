#!/usr/bin/env python2
#-*- coding:utf-8 -*-


"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
       	if s is None or len(s) == 0:
		return ""
	freq = {}
	for e in s:
		f = freq.get(e,0) + 1
		freq[e] = f

	bucket = [[] for i in range(len(s)+1)]
	for e in freq:
		bucket[freq[e]].extend([e] * freq[e])
	res = ""
	for e in bucket[::-1]:
		if len(e) == 0:
			continue		
		res += "".join(e)
	return res

#s = "ababace"
s = "eeeee"
solver = Solution()
res = solver.frequencySort(s)
print res












	
	 

