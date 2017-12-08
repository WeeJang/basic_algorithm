#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 取两个排序数组的中位数(取两个排序数组的第K位数)
"""

def get_middle_of_arrays(array_a,array_b):
	""" middle of arrays """
	
	def find_K_th(k,array_a,array_b,p_as,p_ae,p_bs,p_be):
		print "====K",k,"p_as",p_as,"p_ae",p_ae,"p_bs",p_bs,"p_be",p_be
		len_a = (p_ae -p_as + 1)	
		len_b = (p_be -p_bs + 1) 
		if len_a == 0:
			return array_b[p_bs + k -1]
		if len_b == 0:
			return array_a[p_as + k -1]
		if k == 1:
			if array_a[p_as] <= array_b[p_bs]:
				return array_a[p_as]
			else:
				return array_b[p_bs]
			
		k_a = len_a * k / ( len_a + len_b ) 
		k_b = k - k_a

		print "K",k,"len_a",len_a,"len_b",len_b,"k_a",k_a,"k_b",k_b
		if array_a[p_as + k_a - 1] < array_b[p_bs + k_b - 1]:
			print "drop a",array_a[p_as:p_as + k_a]
			return find_K_th(k - k_a,array_a,array_b,p_as + k_a,p_ae,p_bs,p_bs + k_b - 1)	
		else:
			print "drop b",array_b[p_bs:p_bs + k_b]
			return find_K_th(k - k_b,array_a,array_b,p_as,p_as + k_a -1,p_bs + k_b,p_be)	

	len_a,len_b = len(array_a),len(array_b)
	sum_ = len_a + len_b 
	if sum_ % 2 == 1:
		return find_K_th(sum_/2,array_a,array_b,0,len_a - 1,0,len_b - 1)
	else:
		return 0.5 * (find_K_th(sum_/2,array_a,array_b,0,len_a - 1,0,len_b - 1) + \
			find_K_th(sum_/2+1,array_a,array_b,0,len_a - 1,0,len_b - 1))
			
			
#a = [1,2,4,7,9,11,14,16,20]
a = [1,2,4,7,9,11,14,16]
b = [2,4,6]
print a
print b
print get_middle_of_arrays(a,b)

