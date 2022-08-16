// https://leetcode.com/problems/longest-repeating-character-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s: return 0
        l, r = 0, 0
        memo = {}
        res = 1
        while r < len(s):
            if s[r] not in memo:
                memo[s[r]] = 1
            else:
                memo[s[r]] += 1
            while (r - l + 1 - max(memo.values())) > k:
                memo[s[l]] -= 1
                l += 1
            r += 1
            res = max(res, r - l)
        return res
        