// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0]*n for _ in range(2)]
        if nums[0] > 0: 
            dp[0][0] = nums[0]
        else:
            dp[1][0] = nums[0]
        ans = nums[0]
        for i in range(1, n):
            cur = nums[i]
            temp1 = max(cur, max(dp[0][i - 1]*cur, dp[1][i - 1]* cur))
            dp[0][i] = temp1 if temp1 > 0 else 0
            temp2 = min(cur, min(dp[0][i - 1]*cur, dp[1][i - 1]* cur))
            dp[1][i] = temp2 if temp2 < 0 else 0
            ans = max(ans, dp[0][i])
        return ans