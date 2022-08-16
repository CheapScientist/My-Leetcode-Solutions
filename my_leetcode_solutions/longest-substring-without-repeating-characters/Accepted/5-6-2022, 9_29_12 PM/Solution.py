// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l, r = 0, 0 
        lookup = set()
        while r < len(s):
            if s[r] not in lookup:
                lookup.add(s[r])
                r += 1
            else:
                ans = max(ans, r - l)
                while s[r] in lookup:
                    lookup.remove(s[l])
                    l += 1
        return max(ans, r - l)