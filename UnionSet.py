#!/usr/bin/env python2


class UnionSet(object):

    def __init__(self,set_len):
        self._parent_list_ = list(range(0,set_len))

   
    def root(self,i):
        while self._parent_list_[i] != self._parent_list_[self._parent_list_[i]]:
	    self._parent_list_[i] = self._parent_list_[self._parent_list_[i]]
	return self._parent_list_[i]

    def union(self,i,j):
	self._parent_list_[self.root(i)] = self.root(j)

    def find(self,i,j):
	return self.root(i) == self.root(j)

    def debug(self):
        print self._parent_list_





if __name__ == "__main__":
    us = UnionSet(10)
    us.debug() 
    us.union(1,4)
    us.union(4,9)
    us.union(3,9)
    us.union(2,3)
    us.debug() 
    print us.find(1,2)
    print us.find(1,4)
    print us.find(1,3)
    print us.find(8,3)
 
