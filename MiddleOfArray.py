#!/usr/bin/env python2
#-*- coding:utf-8 -*-


def get_middle_of_arrays(array_a,array_b):
	""" middle of arrays """
	
	start_a,end_a = 0,len(array_a)-1			
	start_b,end_b = 0,len(array_b)-1
	K = (len(array_a) + len(array_b) + 1) / 2 #第K个数
	
	p_a,p_b = -1,-1
	while start_a + 1 < end_a and start_b + 1 < end_b:
		p_a = start_a + (end_a - start_a)/2 #第一个搜索指针
		p_b = K - p_a
		if array_a[p_a] > array_b[p_b]:
			end_a = p_a
			start_b = p_b
		else:
			start_a = p_a
			end_b = p_b
		print(start_a,end_a,start_b,end_b)
	#附近搜索
	target = -1
	if K % 2 == 1:
		#取一个
		while K - p_a:
				
			
			
						
			
c = [1,2,4,7,9,11,14,16,20]
b = [2,4,6]
print get_middle_of_arrays(c,b)

