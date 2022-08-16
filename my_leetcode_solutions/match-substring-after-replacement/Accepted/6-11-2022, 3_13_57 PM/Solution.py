// https://leetcode.com/problems/match-substring-after-replacement

class Solution(object):
	def matchReplacement(self, s, sub, mappings):
		"""
		:type s: str
		:type sub: str
		:type mappings: List[List[str]]
		:rtype: bool
		"""
		n=len(s)
		m=len(sub)
		d=defaultdict(set)
		for x,y in mappings:
			d[x].add(y)
		for i in range(n-m+1):
			found=True
			for j in range(m):
				if s[i+j]!=sub[j]:
					if s[i+j] not in d[sub[j]]:
						found=False
						break
			if found:
				return True
		return False