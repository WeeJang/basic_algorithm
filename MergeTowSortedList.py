#!/usr/bin/env python2
#-*- coding:utf-8 -*-

"“” 有时候真的感觉，递归解法才是王道，清晰，处理边界还好用"""
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        node = None
        if l1.val <= l2.val:
            node = ListNode(l1.val)
            node.next = self.mergeTwoLists(l1.next,l2)
        else:
            node = ListNode(l2.val)
            node.next = self.mergeTwoLists(l1,l2.next)
        return node
            
