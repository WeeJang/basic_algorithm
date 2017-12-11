#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 涉及到的相关问题 three-way-partition """


def find_kth(k,start,end,num_list):
	""" 查找num_list[start,end]中的第k个值 """	
	
	if k < 3: #插入排序
		insert_sorted_list = []
		temp_list = []
		for elem in num_list[start:end+1]:
			print elem,insert_sorted_list
			if len(insert_sorted_list) == 0:
				insert_sorted_list.append(elem)
				continue
			while len(insert_sorted_list) != 0:
				if insert_sorted_list[-1] > elem:
					temp_list.append(insert_sorted_list.pop())
				else:
					break
			insert_sorted_list.append(elem)
			while len(temp_list) != 0:
				insert_sorted_list.append(temp_list.pop())
		return insert_sorted_list[k-1]
	#否则就parition(QuickSort思想) n*log(k)
	i,j = start-1,start-1 #num_list[:i] <= pivot,num_list(i,j] > pivot
	while j < end - start :
 		j += 1
		if num_list[j] <= num_list[end]:
			i += 1
			num_list[i],num_list[j] = num_list[j],num_list[i]

	mid_th = i - start + 1
	#print "mid_th {} i {} k {}".format(mid_th,i,k)
	if mid_th == k:
		return num_list[i]
	elif mid_th < k:
		return find_kth(k-mid_th,i+1,end,num_list)
	else:
		return find_kth(k-1,start,i-1,num_list)


def three_way_partition(num_list):
	list_len = len(num_list)
	#n = list_len / 2
	
	i,j,k = 0,0,list_len - 1
	mid = num_list[-1]
	while j <= k:
		if num_list[j] < mid:
			num_list[i],num_list[j] = num_list[j],num_list[i]
			i += 1
		elif num_list[j] > mid:
			num_list[k],num_list[j] = num_list[j],num_list[k]
			k -= 1
		j += 1
	return num_list	


def make_mapping(n):
	""" (0,1,...n-1) => (1,3,5,..0,2,4) """
	raw_list = list(range(0,n))
	i,j = -1,-1
	while j < n:
		j += 1
		if j % 2 == 1:
			i += 1
			raw_list[i],raw_list[j] = raw_list[j],raw_list[i]
	return raw_list

def make_mapping2(n):
	return [(1+2*i) % (n|1) for i in range(n)]
	
def wiggle_sorted(num_list):
	n = len(num_list)
	M = make_mapping2(n)
	m_th = n / 2
	mid = find_kth(m_th,0,len(num_list)-1,num_list)
	
	i,j,k = 0,0,n - 1
	while j <= k:
		if num_list[M[j]] < mid:
			num_list[M[i]],num_list[M[j]] = num_list[M[j]],num_list[M[i]]
			i += 1
		elif num_list[M[j]] > mid:
			num_list[M[k]],num_list[M[j]] = num_list[M[j]],num_list[M[k]]
			k -= 1
		j += 1
	return num_list	

	

a = [1,5,4,2,3,10,7,4]
#print find_kth(5,0,len(a)-1,a)
#print three_way_partition(a)
#print make_mapping(10)
print wiggle_sorted(a)






