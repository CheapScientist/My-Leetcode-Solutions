// https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                a1 = triangle[i - 1][j - 1] if j > 0 else float('inf')
                a2 = triangle[i - 1][j] if j < len(triangle[i - 1]) else float('inf')
                triangle[i][j] += min(a1, a2)
                
        return min(triangle[-1])

            
        
        