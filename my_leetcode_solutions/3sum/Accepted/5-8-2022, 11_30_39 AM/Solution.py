// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = set()
        def twoSum(nums, l, r, target):
            # here we assume that the input nums is sorted
            # also we wish to remove any duplicates
            ans = []
            while l < r:
                if nums[r] + nums[l] < target:
                    l += 1
                elif nums[r] + nums[l] > target:
                    r -= 1
                else:
                    ans.append([nums[r], nums[l]])
                    # now remove duplicates by incrementing/decrementing l/r
                    while l + 1 < r and nums[l] == nums[l + 1]:
                        l += 1
                    while r - 1 > l and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
            return ans
        
        for idx, num in enumerate(nums):
            if num not in used:
                used.add(num)
                for twoSumRes in twoSum(nums, idx + 1, len(nums) - 1, -num):
                    res.append([num] + twoSumRes)
        return res