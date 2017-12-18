#!/usr/bin/env python2


# DP
# D[i,j] = max { \
#		D[i,j-1],
#		D[i-1,j],
#		D[i-1,j-1] + ( A[i] == B[j] ? 1 : 0 )


def LCS(str_1,str_2):
    str_1_len,str_2_len = len(str_1),len(str_2)
    if str_1_len * str_2_len == 0:
        return 0
    # dummy for [0:],[:0]
    #D = [ [0] * (str_1_len + 1)] * (str_2_len +1)
    D = [ [ 0 for col in range(str_1_len + 1) ] for row in range(str_2_len) ]
    for i in range(1,str_2_len + 1):
        for j in range(1,str_1_len + 1):
            D[i][j] = max(D[i-1][j],D[i][j-1],\
			D[i-1][j-1] + ( 1 if str_2[i-1]==str_1[j-1] else 0 ))
    return D[str_2_len][str_1_len]


print LCS("abcefg","beg")
