// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        ans = 1
        n = len(s)
        res = []
        for m in range(n):
            # odd length
            l, r = m, m
            while l >= 0 and r < n and s[r] == s[l]:
                if r - l + 1 > ans:
                    ans = r - l + 1
                    res = [l, r]
                l -= 1
                r += 1
            
            # even length
            l, r = m, m + 1
            while l >= 0 and r < n and s[r] == s[l]:
                if r - l + 1 > ans:
                    ans = r - l + 1
                    res = [l, r]
                l -= 1
                r += 1
        return s[res[0]:res[1]+1] if ans > 1 else s[0]