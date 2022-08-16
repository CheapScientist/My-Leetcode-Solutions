// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        low, high = 0, len(nums)-1
        first = self.findFirstIndex(nums, low, high, target)

        second = self.findLastIndex(nums, low, high, target)
        
        return [first, second]
    def findFirstIndex(self, nums, low, high, target):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                res = mid
                high = mid-1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return res
    
    def findLastIndex(self, nums, low, high, target):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                res = mid
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return res