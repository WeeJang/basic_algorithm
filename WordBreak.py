#!/usr/bin/env python2
#-*- coding:utf-8 -*-

""""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.


一开始暴力DFS,遇到下面超时，加DP（备忘录机制）

"""



END = "##END##"	
class Trie(object):
	
	def __init__(self,wordDict):
		self.trie = {}
		for word in wordDict:
			p_node = self.trie
			for a in word:
				a_node = p_node.get(a,{})
				if len(a_node) == 0:
					p_node[a] = a_node
				p_node = a_node
			p_node[END] = END
	
	def find(self,target_s):
		#print "find",target_s
		p_node = self.trie
		for a in target_s:
			a_node = p_node.get(a)
			if a_node is None:
				return False
			p_node = a_node
		if END in p_node:
			return True
		else:
			return False	

class Solution(object):

	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: bool
		"""
		if str is None or wordDict is None:
			return False
		if len(wordDict) == 0:
			return False
		trie = Trie(wordDict)
		
		#备忘录[DP] None is not-sure, otherwise True/False
		solution_list = [None for i in range(len(s))]		
	
		def dfs(start_pos):
			""" 从s[start_pos]可以segment-break """
			#print "start_pos",start_pos	
			if start_pos >= len(s):
				#print "###"
				return True
			if solution_list[start_pos] is not None:
				return solution_list[start_pos]
			flag = False	
			for i in range(start_pos + 1,len(s)+1):
				if not trie.find(s[start_pos:i]):
					continue
				#print s[start_pos:i]
				if dfs(i):
					flag = True
					break
			solution_list[start_pos] = flag
			return flag			
		return dfs(0)


s = "leetcode"
wordDict = ["leet", "code"]

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

solver = Solution()	
print solver.wordBreak(s,wordDict)

#trie = Trie(wordDict)
#print trie.trie
#print trie.find("leet")
#print trie.find("leete")

