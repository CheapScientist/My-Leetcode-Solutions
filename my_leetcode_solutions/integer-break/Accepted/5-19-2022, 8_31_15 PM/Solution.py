// https://leetcode.com/problems/integer-break

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dfs(cur):
            if cur in memo:
                return memo[cur]
            if cur == 0:
                return 0
            if cur == 1:
                return 1
            temp = 0
            for i in range(1, cur):
                temp = max(temp, dfs(cur - i)*i, i *(cur - i))
            memo[cur] = temp
            return temp
        
        return dfs(n)
        
        