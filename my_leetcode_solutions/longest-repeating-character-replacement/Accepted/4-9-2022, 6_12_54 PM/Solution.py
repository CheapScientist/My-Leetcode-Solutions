// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lookup = {}
        l = 0
        res = 0
        for right in range(len(s)):
            lookup[s[right]] = 1 + lookup.get(s[right], 0)
            while k + max(lookup.values()) < right - l + 1:
                lookup[s[l]] -= 1
                l += 1
            res = max(res, right - l + 1)
        return res