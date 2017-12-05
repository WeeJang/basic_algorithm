#!/usr/bin/env python2
#-*- coding:utf-8 -*-

## 大整数相乘 ##


def split_str(str_,inter_len):
	ret_list = []
	k = 0
	N = len(str_)
	while k < N :
		ind = N - k 
		start = ind-inter_len
		if start < 0:
			start = 0	
		print start,ind
		target_str = str_[start:ind]
		#print(target_str)
		ret_list.append(int(target_str))
		k += inter_len
	return ret_list[::-1]

def big_interger_mul(int_str_1,int_str_2):
	K = 3
	int_1_list = split_str(int_str_1,K)
	int_2_list = split_str(int_str_2,K)	
	print int_1_list,int_2_list
	int_1_len,int_2_len = len(int_1_list),len(int_2_list)
	print int_1_len,int_2_len
	D = [ [ 0 for col in range(int_2_len) ] for row in range(int_1_len) ]
	print int_1_len,int_2_len,D
	for i in range(int_1_len):
		print "h",i
		for j in range(int_2_len):
			print j,
			D[i][j] = int_1_list[i] * int_2_list[j]

	print("hello")
	print D
	#斜着加
	accum_list = [0 for col in range( int_1_len + int_2_len - 1 )]
	for i in range(len(accum_list)):
		print "i",i
		for j in range(0,i+1):
			print(j,i-j)
			if i-j >= int_2_len:
				continue
			if j >= int_1_len:
				continue
			accum_list[i] += D[j][i-j]	

	#进位
	acc = 0	
	for i in range(len(accum_list)):
		elem = accum_list[i]
		elem += acc
		acc,r = elem / 1000, elem % 1000
		accum_list[i] = r
	if acc != 0:
		accum_list.insert(0,acc)
	return int("".join([str(elem) for elem in accum_list]))

	

print big_interger_mul("123456","4567892")
print "=" * 10
print 123456 * 4567892
