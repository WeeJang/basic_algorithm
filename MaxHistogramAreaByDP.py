#!/usr/bin/env python2
#-*- coding:utf-8 -*-


def get_max_histogram_area(height_list):
	"""  DP
	 A = height_list
	 L : left bound of i A[L[i]:i+1] >= A[i]
	 R : righ bound of i A[i:R[i+1]] >= A[i]
	"""
	A = height_list
	if  A == None or len(A) == 0:
		return 0
	if len(A) == 1:
		return A[0]
	
	L = [0 for i in range(len(A))]
	for ind in range(len(A)):
		if ind == 0:
			continue
		temp = ind #不变式 A[temp] >= A[ind]
		while A[temp-1] >= A[ind]:
			temp = L[temp-1]
			if temp == 0:
				break
		L[ind] = temp
	
	R = [len(A)-1 for i in range(len(A))]
	for ind in range(len(A))[::-1]:
		print "ind",ind
		if ind == len(A) - 1:
			continue
		temp = ind #不变式A[ind] <= A[temp]
		while A[temp+1] >= A[ind]:
			temp = R[temp+1]
			if temp == len(A) - 1:
				break
		R[ind] = temp
	print L
	print R
	max_area = -1				
	for ind in range(len(L)):
		max_area = max(A[ind] * (R[ind] - L[ind] + 1),max_area)
	return max_area
	
a = [2,1,6,4,3]
print get_max_histogram_area(a) # == 9
	
	
