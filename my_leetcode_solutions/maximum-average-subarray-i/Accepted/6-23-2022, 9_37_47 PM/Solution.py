// https://leetcode.com/problems/maximum-average-subarray-i

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k - 1
        ans = float('-inf')
        total = sum(nums[:k-1])
        while r < len(nums):
            total += nums[r]

            ans = max(ans, total/k)
            r += 1
            total -= nums[l]
            l += 1
        return ans
            
            