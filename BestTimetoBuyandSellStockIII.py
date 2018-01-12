#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


P[0:end] = max_i{P[0:i] +  P[i+1:end]}
找到最优分割点i 分割两笔交易

"""

#超时了,时间复杂度0(n^2)
class Solution1(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
	if prices is None or len(prices) <= 1:
		return 0
		
	def handler(i,j):
		""" 获取prices[i:j]的最大利润 """
		if j - i < 2:
			return 0
		min_,profile = float('inf'),0
		for ind in range(i,j):
			if min_ > prices[ind]:
				min_ = prices[ind]
			p_ = prices[ind] - min_
			if p_ > profile:
				profile = p_
		print "{} {} profile {}".format(i,j,profile)
		return profile
	
	max_p = 0
	for i in range(0,len(prices)):
		p = handler(0,i) + handler(i,len(prices))
		if p > max_p:
			max_p = p
	return max_p

"""
DP  p[:end] = max_i{p[:i] + p[i:end]} for i in range(len(p))
"""

class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
	if prices is None or len(prices) <= 1:
		return 0

	#profile[:i] 从第一天到第i天能获得的最大profile	
	profile_l_r = [ 0 for e in range(len(prices)) ] 	
	#profile[i:] 从第i天到最后一天能获得的最大profile	
	profile_r_l = [ 0 for e in range(len(prices)) ] 

	#cal profile_l_r
	max_profile = 0	
	min_price = float('inf')
	for i in range(len(prices)):
		if prices[i] < min_price:
			min_price = prices[i]
		profile = prices[i] - min_price		
		if profile > max_profile:
			max_profile = profile
		profile_l_r[i] = max_profile

	max_profile = 0	
	max_price = float('-inf')
	#cal profile_r_l
	for i in range(len(prices))[::-1]:
		if prices[i] > max_price:
			max_price = prices[i]
		profile = max_price - prices[i]
		if profile > max_profile:
			max_profile = profile
		profile_r_l[i] = max_profile
	#print profile_l_r
	#print profile_r_l
	max_profile = 0
	for i in range(len(prices)):
		p = profile_l_r[i] + profile_r_l[i]
		if p > max_profile:
			max_profile = p
	return max_profile					
	

prices = [2,3,6,1,4,0,3,2,9] 
#prices = [0,1,2,1,4,0,3,2,9] 
solver = Solution()
print solver.maxProfit(prices)









				


	
			
