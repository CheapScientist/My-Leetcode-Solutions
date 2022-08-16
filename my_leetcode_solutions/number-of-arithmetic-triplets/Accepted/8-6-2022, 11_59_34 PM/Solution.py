// https://leetcode.com/problems/number-of-arithmetic-triplets

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n - 2):
            loc1 = bisect_left(nums, nums[i] + diff)

            if loc1 < n and nums[loc1] == nums[i] + diff:
                loc2 = bisect_left(nums, nums[loc1] + diff)
                if loc2 < n and nums[loc2] == nums[loc1] + diff:
                    ans += 1
                    
        return ans
                    