// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        res, n = len(nums), len(nums)
        
        def LIS(nums, direction) -> list[int]:
            dp = [1]
            if direction:
                for i in range(1, len(nums)):
                    temp = 1
                    for j in range(i):
                        if nums[i] > nums[j]:
                            temp = max(temp, 1 + dp[j])
                    dp.append(temp)
                return dp
            else:
                nums = nums[::-1]
                for i in range(1, len(nums)):
                    temp = 1
                    for j in range(i):
                        if nums[i] > nums[j]:
                            temp = max(temp, 1 + dp[j])
                    dp.append(temp)
                return dp[::-1]
        l, r = LIS(nums, True), LIS(nums, False)
        for i in range(1, len(nums) - 1):
            left, right = l[i], r[i]
            if left > 1 and right > 1:
                res = min(res, n - left - right + 1)
        return res