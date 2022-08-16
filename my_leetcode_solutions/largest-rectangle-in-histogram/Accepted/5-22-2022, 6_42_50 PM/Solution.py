// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [(0, -1)] # pair: (index, height)
        heights.append(0)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        heights.pop()
        return maxArea