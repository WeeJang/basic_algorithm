#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
import copy
import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
       	self.origin = nums 

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
	nums_c = copy.deepcopy(self.origin)
	l = len(nums_c)
	for i in range(l):
		j = random.randint(0,l-1)
		nums_c[i],nums_c[j] = nums_c[j],nums_c[i]
	return nums_c
		

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

