#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

"""


class Solution(object):

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
	
	:method
		Using Dynamic Programming(DP)

	D[k][i] meaning the maxinum profile until prices[i] at the most k transaction
	so 
	D[k][j] = max{ D[k][j-1], prices[j] - prices[jj] + D[k-1][jj] for jj in range(0,j) }
                = max{ D[k][j-1], prices[j] + max{ D[k-1][jj] - prices[jj] } } 
        """
		





















					














			

























											




































	





















		       
















 
