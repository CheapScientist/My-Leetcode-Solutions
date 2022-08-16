// https://leetcode.com/problems/restore-ip-addresses

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        build = []

        def valid(s: str):
            if not s:
                return False
            if s == '0':
                return True
            if s.lstrip('0') != s:
                return False
            if not (256 > int(s) >= 0):
                return False
            return True

        def dfs(i, k):
            if len(s) - i > 3*k:
                return 
            if k == 0 and i > (len(s) - 1):
                ans = '.'.join(build)
                res.append(ans)
                return
            for j in range(i, len(s)):
                if valid(s[i:j + 1]):
                    build.append(s[i:j + 1])
                    dfs(j + 1, k - 1)
                    build.pop()
            return

        dfs(0, 4)
        return res