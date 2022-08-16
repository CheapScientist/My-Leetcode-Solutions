// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [(-1, -1)]
        heights.append(0)
        
        for idx, height in enumerate(heights): 
            start = idx
            while stack and stack[-1][0] > height:
                prevHeight, prevIdx = stack.pop()
                res = max(res, prevHeight*(idx - prevIdx))
                start = prevIdx
            stack.append((height, start))
        heights.pop()
        return res