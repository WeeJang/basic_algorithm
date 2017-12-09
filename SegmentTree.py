#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" 线段树（区间树) """


"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
	self.count = 0
"""


class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        # write your code here
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start,end)
        node = SegmentTreeNode(start,end)
        mid = start + (end - start) / 2
        node.left = self.build(start,mid)
        node.right = self.build(mid+1,end)
        return node


   def query(self, root, start, end):
        #print (start,end)
        # write your code here
        if root == None:
            return 0
        if start <= root.start and end >= root.end:
            return root.count
        mid = (root.start + root.end) / 2
        if end <= mid:
            return self.query(root.left,start,end)
        if start > mid:
            return self.query(root.right,start,end)
        else:
            return self.query(root.left,start,mid) + self.query(root.right,mid+1,end)
