// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l, ans = 0, 1
        seen = set()
        
        for r in range(len(s)):
            while l <= r and s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            ans = max(ans, r - l + 1)
        return ans