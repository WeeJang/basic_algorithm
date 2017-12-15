#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 计数排序 
      1)线性时间排序
      2)思考一个问题哈？为什么一个计数排序搞的这么复杂。
        我所谓的复杂就是为什么先求累加和，然后再确定位置。
        如果简单的计数排序，直接#计数完后，直接根据个数构建T就可以啦(复制数据排序数据)
        原因是：为了保证计数的排序的稳定性（无论多少次排序，相对位置是确定的（相同的数据但卫星数据不同））
	
	当计算完累计值之后，注意从原数组(nums)从后向前取数据，然后去C数组里面找它对应的位置，放在T中，并将
        数据的C值进行更新。这样保证了稳定性。
"""

def count_sort(k,nums):
	"""
	   k : 代表nums 中的最大值，nums中的数值属于[0,k]
	"""
	C = [ 0 for i in range(0,k+1) ]  #计数数组
	T = [ 0 for i in range(len(nums)) ] #排序后的数组
	
	#计数	
	for elem in nums:
		C[elem] += 1
	# 累加 C[i] 代表nums中小于等于i的数目有多少
	#  也就代表值“i"排在T的第(C[i])个位置（坐标为C[i]-1)
	for i in range(1,len(C)):
		C[i] += C[i-1]
	#!!!
	#
	for i in range(len(nums))[::-1]:
		T[C[nums[i]]-1] = nums[i]
		C[nums[i]] -= 1 #因为含有相同的元素
	return T

nums = [0,2,1,4,2,3,0] 
print count_sort(4,nums)		 	
	
	


