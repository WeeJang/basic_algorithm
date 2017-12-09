#!/usr/bin/env python2
#-*- coding:utf-8 -*-

class Solution:
    """
    @param: strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        if strs is None or len(strs) == 0:
            return ""
        counter = 0
        for ind in range(min([len(elem) for elem in strs])):
            if len(set([elem[ind] for elem in strs])) == 1:
                counter += 1
                continue
            break
        return strs[0][:counter]
