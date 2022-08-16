// https://leetcode.com/problems/longest-ideal-subsequence

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
            m = {}
            res = 1
            for c in s:
                mx = 0
                for i in range(-k, k+1):
                    cur = chr(ord(c)+i)
                    if 'a' <=cur <= 'z' and cur in m:
                        mx = max(mx, m[cur])
                m[c] = mx+1
                res = max(res, m[c])
            return res