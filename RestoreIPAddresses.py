#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""


class Solution(object):
	def restoreIpAddresses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		def is_legal(seg_s):
			if seg_s[0] == '0':
				if len(seg_s) == 1:
					return True
				else:
					return False
			seg_int = int(seg_s)
			if seg_int > 255:
				return False
			return True	
								
		def dfs(start_pos,k):
			""" s[start_pos:]能够组成k段合法ip（合法ip四段)"""
			if start_pos == len(s) and k == 0:
				return True,[[]]
			if k == 0 and start_pos != len(s):
				return False,[[]]
			if k != 0 and start_pos >= len(s):
				return False,[[]]
			ret = []
			flag = False
			for i in range(start_pos+1,len(s)+1):
				is_l = is_legal(s[start_pos:i])
				print s[start_pos:i],is_l
				if not is_l:
					continue
				res = dfs(i,k-1)
				if res[0]:
					flag = True
					for r in res[1]:
						c = [s[start_pos:i]]
						c.extend(r)
						ret.append(c)
			return flag,ret
		r = dfs(0,4)
		pure_ret = r[1]
		if pure_ret == [[]]:
			return []
		for i in range(len(pure_ret)):
			pure_ret[i] = ".".join(pure_ret[i])
		return pure_ret

#str_ = "25525511135"
#str_ = "010010"
str_ = ""
solver = Solution()	
print solver.restoreIpAddresses(str_)







	
        


