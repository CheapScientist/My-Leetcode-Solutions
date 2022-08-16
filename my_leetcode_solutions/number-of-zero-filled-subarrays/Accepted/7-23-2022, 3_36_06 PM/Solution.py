// https://leetcode.com/problems/number-of-zero-filled-subarrays

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = r = 0
        n = len(nums)

        while r < n:
            l = r
            while r < n and nums[r] == 0:
                ans += (r - l + 1)
                r += 1
            r += 1
        return ans