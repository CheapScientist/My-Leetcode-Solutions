// https://leetcode.com/problems/arithmetic-slices

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3: return 0
        n = len(nums)
        dp = [0]*n
        for i in range(1, n):
            dp[i] = nums[i] - nums[i - 1]
        ans = 0
        l, r = 1, 1
        
        def helper(num):
            if num < 2: return 0
            return (num*(num - 1))//2
        
        while r < n:
            prev = dp[l]
            while r + 1 < n and dp[r + 1] == prev:
                r += 1
            ans += helper(r - l + 1)
            r += 1
            l = r
        return ans
        