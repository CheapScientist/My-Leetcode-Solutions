// https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r: 
            mi = (l + r)//2
            if nums[mi] == target: return mi
            if nums[l] == target: return l
            if nums[r] == target: return r
            
            # if left portion is sorted: 
            if nums[l] < nums[mi]: 
                if nums[mi] > target > nums[l]:
                    r = mi - 1
                else:
                    l = mi + 1
            else:
            # if right portion is sorted: 
                if nums[r] > target > nums[mi]:
                    l = mi + 1
                else:
                    r = mi - 1
        return -1