// https://leetcode.com/problems/repeated-dna-sequences

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10: return []
        l, r = 0, 10
        ans, lookup = set(), {}
        while r <= n:
            temp = s[l:r]
            lookup[temp] = lookup.get(temp, 0) + 1
            if lookup[temp] > 1:
                ans.add(temp)
            l += 1
            r += 1
        return list(ans)
            