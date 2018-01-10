#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""


class Solution(object):

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
	if people is None:
		return []
	if len(people) == 1 and len(people[0]) == 0:
		return []	       
	result = []
	
	#先按照h排序（从大到小），然后按照p排序,从小到大
	def cmp(a,b):
		if a[0] - b[0] != 0:
			return b[0] - a[0]
		return a[1] - b[1]
	people = sorted(people,cmp = cmp)
	#print people	
	#insert elem : (h,k)
	for e in people:
		#find index
		result.insert(e[1],e)
	return result




people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
result = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
solver = Solution()
res = solver.reconstructQueue(people)
print res
print result
 



















