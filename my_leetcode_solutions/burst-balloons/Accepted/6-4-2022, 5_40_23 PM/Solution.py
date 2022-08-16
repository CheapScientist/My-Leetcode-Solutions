// https://leetcode.com/problems/burst-balloons

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        
        def dfs(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l > r:
                memo[(l, r)] = 0
                return 0
            res = 0
            for i in range(l, r + 1):
                pivot = nums[i]
                left = nums[l - 1]
                right = nums[r + 1]
                res = max(res, dfs(l, i - 1) + dfs(i + 1, r) + pivot*left*right)
            memo[(l, r)] = res
            return res
        return dfs(1, len(nums) - 2)