// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if not m or not n: return 0
        up = [1]*n
        for r in range(1, m):
            temp = [1]*n
            for c in range(1, n): 
                temp[c] = temp[c - 1] + up[c]
            up = temp[:]
        return up[-1]