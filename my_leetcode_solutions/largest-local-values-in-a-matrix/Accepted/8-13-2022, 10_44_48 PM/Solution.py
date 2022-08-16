// https://leetcode.com/problems/largest-local-values-in-a-matrix

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []
        for r in range(n - 2):
            temp = []
            for c in range(n - 2):
                temp2 = float('-inf')
                for x in range(r, r + 3):
                    for y in range(c, c + 3):
                        temp2 = max(temp2, grid[x][y])
                temp.append(temp2)    
            ans.append(temp[:])
        return ans