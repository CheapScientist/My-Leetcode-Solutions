// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix, target: int):
        first_column = []
        for i in matrix:
            first_column.append(i[0])
        l = self.binarySearch(first_column, target)
        return self.binarySearch2(matrix[l], target)
    def binarySearch(self, nums, target):
        l ,r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l - 1
    def binarySearch2(self, nums, target):
        l ,r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False