// https://leetcode.com/problems/single-element-in-a-sorted-array

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums) - 1 # [inclusive, inclusive]
        while l <= r: 
            mi = (l + r)//2
            if (mi - 1 >= 0 and nums[mi - 1] == nums[mi]) or (mi + 1 < len(nums) and nums[mi + 1] == nums[mi]):
                if nums[mi - 1] == nums[mi]: 
                    if (mi + 1) % 2 == 1: 
                        r = mi - 1
                    else:
                        l = mi + 1
                else:
                    if (mi) % 2 == 1: 
                        r = mi - 1
                    else:
                        l = mi + 1
            else: 
                return nums[mi]
        return -1
            
            