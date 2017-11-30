#!/usr/bin/env python2
#-*- coding:utf-8 -*-



def isMatch(s,p):

	len_s,len_p = len(s),len(p)
	if len_s * len_p == 0:
		return False
	
	D = [ [0] * len_s ] * len_p # len_p * len_s
	
	def _inner_match_for_d(p_p,p_s):
		if p[p_p] == ".":
			return True
		if p[p_p] == "*" and p[p_p - 1] == ".":
			return True
		if p[p_p] == "*" and p[p_p - 1] != ".":
			return p[p_p - 1] == s[p_s]
				
