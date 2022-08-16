// https://leetcode.com/problems/unique-binary-search-trees

class Solution:
    def numTrees(self, n: int) -> int:
        # transition function works like: f(3) = f(0)*f(3 - 1) + f(1)*f(3 - 2) + f(2) *f(3- 3)
        # so initialize dp
        dp = [0]*(n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            temp = 0
            for j in range(i + 1):
                temp += dp[j]*dp[i - 1 - j]
            dp[i] = temp
        return dp[-1]