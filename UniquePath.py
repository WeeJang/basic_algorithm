#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

m and n will be at most 100.

"""

def get_unique_path(m,n):
	""" DP[m,n] = D[m-1,n] + D[m,n-1] """

	def helper(m,n):
		if m == 1 or n == 1:
			return 1
		return helper(m-1,n) + helper(m,n-1)
	
	return helper(m,n)
				
print get_unique_path(4,5)



































