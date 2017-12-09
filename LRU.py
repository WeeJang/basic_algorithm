#!/usr/bin/env python2
#-*- coding:utf-8 -*-


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.kv = {}
        self.queue = []

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.kv:
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.kv[key]
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.kv:
            self.kv[key] = value
            self.get(key)  #! 注意，这个地方容易忽略
            return
        self.kv[key] = value
        if len(self.queue) == self.capacity:
            r_elem = self.queue.pop(0)
            self.kv.pop(r_elem)
        self.queue.append(key)
