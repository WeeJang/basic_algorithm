#!/usr/bin/env python2
#-*- coding:utf-8 -*-


""" find kth by recursion """

def find_kth(nums,k):
	""" recursion """
	
	def find_k_(nums,start,end,k):
		if k == 1:
			return max(nums[start:end+1])
		#invariant:nums[:i] <= pivot,nums(i,j] >pivot,nums(j:] = unk
		pivot = nums[end]
		i,j = start - 1,start - 1
		while j < end - 1:
			j += 1
			if nums[j] <= pivot:
				i += 1
				nums[i],nums[j] == nums[j],nums[i]
		# len of (<=pivot)
		len_le = ( i - start + 1 )
		if len_le == k:
			return pivot
		elif len_le > k:
			return find_k_(nums,start,end-1,k-1)
		else:
			return find_k_(nums,start+len_le,end,k-len_le)

	return find_k_(nums,0,len(nums)-1,k)

a = [2,4,1,3,8]
print find_kth(a,3)
		
				
					
					

