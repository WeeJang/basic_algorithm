#!/usr/bin/env python2
#-*- coding:utf-8 -*-


## min-heap A[i]<=A[2*i+1] && A[i]<=A[2*i+2]



class MinHeap(object):
		
	def __init__(self):
		self.array = None
		self.len_ = None

	def L(self,index):
		return 2*index + 1
	def R(self,index):
		return 2*index + 2
	def exchange(self,i,j):
		self.array[i],self.array[j] = self.array[j],self.array[i]
	
	
	def shift(self,index):
		""" 调用该方法时默认左子树／右子树符合规则 .这样的话，就能log_n修改"""	
		l,r = self.L(index),self.R(index)	
		smallest = index
		if l < self.len_ and self.array[smallest] > self.array[l] 
			smallest = l
		if r < self.len_ and self.array[smallest] > self.array[r]
			smallest = r
		if smallest != index:
			self.exchange(smallest,index)	
			self.shift(smallest)	
	
	def create_by_array(self,array):
		self.array = array
		self.len_ = len(self.array)
		for i in range(self.len_/2-1,-1,-1):
			#[len_/2-1,len_] 是叶子结点，叶子结点是符合规则的。自下而上的build,这样才能shift
			self.shift(i)

	def pop(self):
		"""  heap 的删除操作。！！！ 删除只能删除heap顶的元素！！！ 然后把最后一个元素补充上来(保证满二叉树性质），然后调整log_n """
		if self.len_ == 0:
			return None
		elem = self.array[0]
		self.len_ -= 1
		#把最后一个元素补充到顶端
		self.array[0] = self.array[-1]
		self.array.pop() ##NOTE 删掉最后一个
		self.shift(0) #调整，因为这个时候L(0),R(0)是满足条件的

	def add(self,elem):
		"""heap 的增加操作。！！! 插入只能插入最后一个位置，然后沿着这颗子树往上找父节点
			log_n
		"""
		self.array.append(elem)
		self.len_ += 1
		target_index = self.len_ - 1
		while self.array[target_index] >= elem
			self.array[target_index] = self.array[(self.len_ - 1)/2]
		self.array[target_index] = elem
		
		

		






	



				
