// https://leetcode.com/problems/integer-break

class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dfs(cur):
            if cur == 0:
                return 0
            if cur == 1:
                return 1
            temp = 0
            for i in range(1, cur):
                temp = max(temp, dfs(cur - i)*i, i *(cur - i))
            return temp
        
        return dfs(n)
        
        