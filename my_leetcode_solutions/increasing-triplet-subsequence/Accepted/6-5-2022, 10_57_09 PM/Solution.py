// https://leetcode.com/problems/increasing-triplet-subsequence

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        leftMin, rightMax = [], []
        lmin, rmax = float('inf'), float('-inf')
        for i in range(len(nums)):
            l, r = i, len(nums) - i - 1
            leftMin.append(min(lmin, nums[l]))
            rightMax.append(max(rmax, nums[r]))
            lmin = min(lmin, nums[l])
            rmax = max(rmax, nums[r])

        for i in range(1, len(nums) - 1):
            num = nums[i]
            r = len(nums) - i - 1
            lm, rm = leftMin[i - 1], rightMax[r]
            if lm < num < rm:
                return True
        return False
        
        