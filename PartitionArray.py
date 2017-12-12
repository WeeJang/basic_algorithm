#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 数组划分 
	three-way-partition
"""



def partition_array(num_list,k):

	#invariant num_list[:i] < k,num_list(i,j] = k,num_list(j,m] = unk,num_list(m:] > k		
	i,j,m = -1,-1,len(num_list)
	while j < m - 1:
		print "==>",num_list,i,j,m
		j += 1
		if num_list[j] < k:
			i += 1
			num_list[i],num_list[j] = num_list[j],num_list[i]
		elif num_list[j] > k:
			m -= 1
			num_list[m],num_list[j] = num_list[j],num_list[m]
			j -= 1
		else:
			j+=1
	return num_list,i

nums = [1,5,2,8,3,4,1,3]
k = 2
print partition_array(nums,k)
			
				
