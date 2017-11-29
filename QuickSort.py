#!/usr/bin/env python2

def quick_sort(int_list):
	def _qs_(int_list,start_pos,end_pos):
		print(start_pos,end_pos,int_list)
		if start_pos >= end_pos -1:
			return -1
		# int_list[j:end_pos] > int[start_pos]
		j = -1 
		for i in range(start_pos,end_pos):
			if int_list[i] > int_list[start_pos]:
				if j == -1:
					j = i
			else:
				if j == -1:
					continue
				int_list[j],int_list[i] = int_list[i],int_list[j] 
				j += 1
		if j == -1:
			j = end_pos
		int_list[start_pos],int_list[j-1] = int_list[j-1],int_list[start_pos]	 
		_qs_(int_list,start_pos,j-1)
		_qs_(int_list,j,end_pos)
 
	_qs_(int_list,0,len(int_list))		  
   

a = [6,3,2,10,4]
quick_sort(a)  
print(a)
