// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r: 
            mi = (l + r)//2
            if nums[mi] == target: return mi
            if nums[l] <= nums[mi]: 
                if target > nums[mi] or target < nums[l]:
                    l = mi + 1
                else:
                    r = mi - 1
            else:
                if target < nums[mi] or target > nums[r]:
                    r = mi - 1
                else:
                    l = mi + 1
        return -1