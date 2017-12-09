#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""
增加Dummy避免边界问题。
"""

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: head: a ListNode
    @param: val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        if head is None:
            return None
        dummy = ListNode(val + 1)
        dummy.next = head
        p_node = dummy
        while p_node:
            if p_node.next == None:
                break
            if p_node.next.val == val:
                p_node.next = p_node.next.next
            else:
                p_node = p_node.next
        return dummy.next
            
        
