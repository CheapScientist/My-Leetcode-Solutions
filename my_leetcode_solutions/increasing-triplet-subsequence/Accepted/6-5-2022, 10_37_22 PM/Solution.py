// https://leetcode.com/problems/increasing-triplet-subsequence

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        d = []
        for i in range(len(nums)):
            if not d or d[-1] < nums[i]:
                d.append(nums[i])
            else:
                loc = bisect_left(d, nums[i])
                d[loc] = nums[i]
            if len(d) >= 3:
                return True
        return False
        