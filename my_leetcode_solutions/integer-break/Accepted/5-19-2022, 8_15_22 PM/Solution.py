// https://leetcode.com/problems/integer-break

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n + 1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n + 1):
            temp = 0
            for j in range(i):
                temp = max(temp, dp[i - j]*(j), j*(i - j))
            dp[i] = temp
        print(dp)
        return dp[-1]
        
        