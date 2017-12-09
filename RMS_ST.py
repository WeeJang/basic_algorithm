#!/usr/bin/env python2
#-*- coding:utf-8 -*-


""" 
   RMQ(Range Minimum/Maximum Query) 
   求区间最值问题。这里的区间是静态的，里面的元素数值等无法变动 

   下面以求任意区间的最大值为例.
"""



import math

def create_st(num_list):
	""" 区间，返回ST """
	len_l = len(num_list)
	log_len_l = int(math.log(len_l,2))
	#D[i][j] means Max(num_list[i:i+2^j) )
	D = [ [0 for col in range(log_len_l+1)] for row in range(len_l) ]
	
	for i in range(len_l):
		D[i][0] = num_list[i]
	
	for j in range(1,log_len_l+1): #j_th
		for i in range(len_l): #i_th
			if ( i + (1<<j) ) > len_l:
				break 
			#D[i][j] = max( A[i:i+2**j) )
			#        = max( A[i:i+2**(j-1),A[i+2**(j-1),i+2**j) )
			#        = max( A[i:i+2**(j-1),A[i+2**(j-1),i+2**(j-1)*2 )
			#        = max( A[i:i+2**(j-1),A[i+2**(j-1),i+2**(j-1) + 2**(j-1) )
			#        = max( D[i][j-1],D[i+2**(j-1)][j-1] )
			print i,j,1<<(j-1)
			D[i][j] = max(D[i][j-1],D[i+(1<<(j-1))][j-1])
	return D


def query(sparse_table,start,end):
	""" search max of [start,end] """
	D = sparse_table
	len_num = len(sparse_table)
	if start > len_num - 1:
		return None
	if end > len_num - 1:
		return None
	len_s = end - start + 1	
	log_len_s = int(math.log(len_s,2))
	#max(A[start:end]) = max(A[start:start+2**j],A[end-2**j][end-2**j+2**j])
	#                  = max(D[start][j],D[end-2**j][j])
	#  So should : start + 2**j >= end - 2**j  
	#              end - start <= 2**(j+1)
        #                 j >= log(end - start) - 1
	print start,end,1<<log_len_s
	print start,log_len_s,end-(1<<log_len_s)+1,log_len_s
	# 注意 D是左闭右开，查询是双闭
	return max(D[start][log_len_s],D[end-(1<<log_len_s)+1][log_len_s])	
		
def query_max(num_list,index_list):
	a = range(0,5)
	st = create_st(a)
	print "==" * 10
	print st
	print "==" * 10
	for ind in index_list:
		print ind,
		print query(st,ind[0],ind[1])

a = range(0,5)
ind_list = [(0,2),(2,4),(0,3),(0,4)]
query_max(a,ind_list)	
