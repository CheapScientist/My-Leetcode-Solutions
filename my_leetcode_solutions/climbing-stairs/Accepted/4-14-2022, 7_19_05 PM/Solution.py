// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [1, 2]
        count = 2
        while n > count:
            dp.append(dp[count - 1] + dp[count - 2])
            count += 1
        return dp[-1]