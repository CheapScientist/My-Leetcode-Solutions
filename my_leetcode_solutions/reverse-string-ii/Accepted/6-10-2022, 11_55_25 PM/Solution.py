// https://leetcode.com/problems/reverse-string-ii

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s: return ''
        if not k: return s
        res = []

        def dfs(i):
            if i >= len(s):
                return
            res.append(s[i:i + k][::-1])
            res.append(s[i + k:i + 2*k])
            dfs(i + 2*k)
        dfs(0)
        return ''.join(res)