#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""" Trick : Stack """

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: headA: the first list
    @param: headB: the second list
    @return: a ListNode
    """
    def get_stack(self,head):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        return stack
    
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if headA is None or headB is None:
            return None
        interset = None
        stackA,stackB = self.get_stack(headA),self.get_stack(headB)
        while len(stackA) and len(stackB):
            A , B = stackA.pop(),stackB.pop()
            if A.val == B.val:
                interset = A
            else:
                break
        return interset
