#!/usr/bin/env python2

def lowbit(x):
	return x & (-x)

class TreeArray(object):
	
	def __init__(self,n):
		self.__n__ = n
		self.__array__ = [ 0 ] * ( n + 1 )

	def update(self,index,value):
		assert index <= self.__n__
		while index <= self.__n__:
			print "modify index",index
			self.__array__[index] += value
			index += lowbit(index)
	
	def query(self,index):
		assert index <= self.__n__
		sum_ = 0
		while index >= 0:
			sum_ += self.__array__[index]
			index -= lowbit(index)
		return sum_	

	def debug(self):
		print self.__array__

a = TreeArray(16)
a.update(4,4)
print(a.debug())
print a.query(4)
print a.query(7)
print a.query(16)
a.update(8,3)
print(a.debug())
print a.query(4)
print a.query(7)
print a.query(16)

