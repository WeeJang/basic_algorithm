#!/usr/bin/env python2
#-*- coding:utf-8 -*-

# DP
# D[i,j] = min { \
#		D[i,j-1] + 1 , #A[:i] 调整到 B[:j-1]需要的代价+ 在A[i]后面添加B[j]
#		D[i-1,j] + 1,  #A[:i-1] 调整到B[:j]需要的代价 + 删除A[i]的代价
#		D[i-1,j-1] + ( A[i] == B[j] ? 0 : 1 ) #A[:i-1]调整到B[:j-1]需要的代价 + 如果A[i] == B[j]不要付出代价，否则改变A[i] == B[j]


def get_edit_distance(str_1,str_2):
    str_1_len,str_2_len = len(str_1),len(str_2)
    if str_1_len * str_2_len == 0:
        return 0
    # dummy for [0:],[:0]
    #D = [ [0] * (str_1_len + 1)] * (str_2_len + 1)
    #D[i,j] mean distance A[:i) to B[:j)
    D = [ [ 0 for col in range(str_1_len + 1) ] for row in range(str_2_len + 1) ]
   
    #初始化表非常重要
    for i in range(len(D)):
	D[i][0] = i
    for j in range(len(D[0])):
	D[0][j] = j

    for i in range(1,str_2_len + 1): #i代表的step,就是步长，意味着问题规模。问题规模从小到大
        for j in range(1,str_1_len + 1): #j代表的启始位置
            D[i][j] = min(D[i-1][j]+1,D[i][j-1]+1,\
			D[i-1][j-1] + ( 0 if str_2[i-1]==str_1[j-1] else 1 ))
    print D
    return D[str_2_len][str_1_len]


print get_edit_distance("abcefg","beg")
print get_edit_distance("kitten","sitting")
