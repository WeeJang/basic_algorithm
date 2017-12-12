#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" O(n) find the maxgap of array(after sorted) """

""" 线性时间排序:基数／计数／桶排序 """

import math

"""
分析问题：
   num_list一共有n个数,将数轴[a,b]切成了n-1段。
   设最大gap为G,G >= T.如果T<(b-a)/(n-1),则 (n-1)*[(b-a)/(n-1)] < (b-a),显然是不成立的。
   因此G的lowbound必然大于等于(b-a)/(n-1).
   所以，将全部数据进行bucket_sort，然后，同一个桶里面的肯定不是（因为同一个桶里<(b-a)/(n-1),左闭右开区间，不能取等于).所以一定是在在不同的相邻桶中.
   题目中都是整数，因此 T = math.ceil((b-a)/(n-1))

"""

def bucket_sort(num_list):
	"""  bucket-sort  """
	a,b = min(num_list),max(num_list)
	n = len(num_list)
	bucket_size = int(math.ceil((b-a) / (n-1))) #上取整
	bucket_num = (b-a) / bucket_size + 1 
	bucket_list = [ None for i in range(bucket_num)] #[(min,max)]

	print "bucket_size {} bucket_num {} ".format(bucket_size,bucket_num)	
	for elem in num_list:
		bucket_id = (elem - a) / bucket_size
		bucket_elem = bucket_list[bucket_id]
		if bucket_elem == None:
			bucket_elem = [elem,elem]	
		elif bucket_elem[0] > elem:
			bucket_elem[0] = elem
		elif bucket_elem[1] < elem:
			bucket_elem[1] = elem
		bucket_list[bucket_id] = bucket_elem
	#print bucket_list	
	return bucket_list
		
def get_max_gap(num_list):
	bucket_list = bucket_sort(num_list)
	last_bucket = None
	max_gap =  -1
	for bucket in bucket_list:
		if last_bucket == None:
			last_bucket = bucket
			continue
		if bucket == None:
			continue
		gap = bucket[0] - last_bucket[1]
		if gap > max_gap:
			max_gap = gap
		last_bucket = bucket
	return max_gap
a = [ 3,2,9,6,7,1,13]
#bucket_sort(a)
print get_max_gap(a)
























