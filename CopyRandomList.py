#!/usr/bin/env python2
#-*- coding:utf-8 -*-


"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:

    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return None
        new_root = RandomListNode(head.label)
        p_old = head.next
        p_new = new_root
        while p_old:
            new_elem = RandomListNode(p_old.label)
            p_new.next = new_elem
            p_new = new_elem
            p_old = p_old.next
        
        p_old = head
        p_new = new_root
        while p_old:
            if p_old.random == None:
                continue
            p_o,p_n = p_old,p_new
            while p_o.next != p_old.random:
                p_o = p_o.next
                p_n = p_n.next
            p_new.random = p_n.next
            p_new = p_new.next
            p_old = p_old.next
        return new_root
        
        
        
        
        
        
        
        
        
        
        
