#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

简单的O(m+n) space, 两个数组分别记录行坐标，列坐标

要求 常数空间复杂度
"""

class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
	#其实优化就是用原来的内存存这些东西
	#一个array表示哪些列置为0,一个array表示哪些行置为0
	#所以可以直接使用matrix本身来记录
	#比如matrix[i][:] 记录列 matrix[:][j]记录行
	#第一步先搜寻i,j
	if matrix is None:
		return

	z_i,z_j = -1,-1	
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] != 0:
				continue
			if z_i == -1:
				z_i,z_j = i,j
			else:
				matrix[z_i][j] = 0
				matrix[i][z_j] = 0
	if z_i == -1:
		return
	#print z_i,z_j
	#print matrix
	#沿着matrix[z_i][z_j]所在十字按行／列涂改
	#按行(注意留下matrix[z_i][:],最后一步再进行处理）
	for i in range(len(matrix)):
		if i == z_i:
			continue
		if matrix[i][z_j] != 0:
			continue
		for j in range(len(matrix[0])):
			#note 
			matrix[i][j] = 0
	#按照列
	for j in range(len(matrix[0])):
		if matrix[z_i][j] != 0:
			continue
		for i in range(len(matrix)):
			matrix[i][j] = 0
	#处理matrix[z_i][:]
	for j in range(len(matrix[0])):
		matrix[z_i][j] = 0	

	#print matrix	







































#m = [[1,2,0],[1,2,1],[0,1,1]]
m = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
print m
solver = Solution()
solver.setZeroes(m)








