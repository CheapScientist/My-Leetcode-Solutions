// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        l = 0
        # try to extend the range [i, j]
        for r in range(n):
            if s[r] in mp:
                l = max(mp[s[r]], l)
            ans = max(ans, r - l + 1)
            mp[s[r]] = r + 1
        return ans