#!/usr/bin/env python2
#-*- coding:utf-8 -*-
""" 统计小于某些数的个数"""


class Solution:
    """
    @param: A: An integer array
    @param: queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # write your code here
        counter = {}
        max = float("-inf")
        min = float("inf")
        for elem in A:
            c = counter.get(elem,0)
            counter[elem] = c + 1
            if elem > max:
                max = elem
            if elem < min:
                min = elem
        segtree = build_segment_tree(min,max,counter)
        return [query(segtree,elem) for elem in queries]
        


class SegmentTreeNode(object):
    def __init__(self,start,end,counter = 0):
        self.start,self.end,self.counter = start,end,counter
        self.left,self.right = None,None


def build_segment_tree(start,end,counter):
    #print start,end
    if start == end:
        return SegmentTreeNode(start,end,counter.get(start,0))
    root = SegmentTreeNode(start,end)
    mid = (start + end) / 2
    left = build_segment_tree(start,mid,counter)
    right = build_segment_tree(mid + 1,end,counter)
    root.counter = left.counter + right.counter
    root.left,root.right = left,right
    #print "counter",root.counter,root.start,root.end
    return root
    
def query(segtree,elem):
    if segtree is None:
        return 0
    print "query",segtree.start,segtree.end,elem
    if elem <= segtree.start:
        return 0
    if elem > segtree.end:
        return segtree.counter
    return query(segtree.left,elem) + query(segtree.right,elem)

solver = Solution()
a = [1,2,3,4,5,6]
b = [1,2,3,4] 
print solver.countOfSmallerNumber(a,b)
