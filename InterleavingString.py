#!/usr/bin/env python2
#-*- coding:utf-8 -*-

def solution(s1,s2,s3):
	"""  (s1,s2) -> s3 """


	def helper(s1,s2,s3):
		if all((len(s1) == 0,len(s2) == 0,len(s3) == 0)):
			return True
		
		s1_test,s2_test = False,False	
		if len(s1) * len(s3) != 0:
			s1_test = (s1[0] == s3[0] and helper(s1[1:],s2,s3[1:]))
		if len(s2) * len(s3) != 0:
			s2_test = (s2[0] == s3[0] and helper(s1,s2[1:],s3[1:]))
		return s1_test or s2_test
	
	return helper(s1,s2,s3)


print solution("aabcc","dbbca","aadbbcbcac")
print solution("aabcc","dbbca","aadbbbaccc")
