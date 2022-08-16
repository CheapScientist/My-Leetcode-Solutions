// https://leetcode.com/problems/subarray-product-less-than-k

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        ans = 0
        left = 0
        for right, num in enumerate(nums):
            prod *= num
            while left <= right and prod >= k: 
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans