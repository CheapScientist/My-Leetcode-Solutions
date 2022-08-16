// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        leftPointer = 0
        rightPointer = len(height)-1
        while leftPointer < rightPointer:
            area = min(height[leftPointer], height[rightPointer]) * (rightPointer - leftPointer)
            maxWater = max(maxWater, area)
            if height[leftPointer] > height[rightPointer]:
                rightPointer -= 1
            else:
                leftPointer += 1
        return maxWater