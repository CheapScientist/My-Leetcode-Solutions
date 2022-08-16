// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l, r = 0, 0 
        memo = set()
        res = 1
        while r < len(s):
            if s[r] in memo:
                res = max(res, r - l)
                while s[r] in memo:
                    memo.remove(s[l])
                    l += 1
            
            memo.add(s[r])
            r += 1
        return max(res, r - l)
                    