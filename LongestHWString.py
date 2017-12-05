#!/usr/bin/env python2
#-*- coding:utf-8 -*-

def get_longest_hw(str_,start_pos,end_pos):
	
	if start_pos > end_pos :
		return 1
	if start_pos == end_pos:
		return 1
	
	if str_[start_pos] == str_[end_pos]:
		return 2 + get_longest_hw(str_,start_pos+1,end_pos-1)	
	
	else:
		return max(get_longest_hw(str_,start_pos,end_pos-1),get_longest_hw(str_,start_pos+1,end_pos))

c = "aemjhqiewza"
print get_longest_hw(c,0,len(c)-1)



