#!/usr/bin/env python2

#beautiful code

def QS(int_list,start_pos,end_pos):
	if start_pos >= end_pos:
		return
	j,i = start_pos -1,start_pos
	while i <= end_pos:
		if int_list[i] <= int_list[end_pos]:
			j += 1
			int_list[j],int_list[i] = int_list[i],int_list[j]
                i += 1
	QS(int_list,start_pos,j-1)
	QS(int_list,j+1,end_pos)


#a = [10,4,3,9,14]
a = [10,4]
QS(a,0,len(a)-1)
print(a)
