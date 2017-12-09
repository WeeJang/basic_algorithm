#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"""检测环，快慢指针 """

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head is None:
            return False
        slow_p,fast_p = head,head.next
        while True:
            if fast_p == None:
                return False
            if slow_p == fast_p:
                return True
            if fast_p.next == None:
                return False
            fast_p = fast_p.next.next
            slow_p = slow_p.next
