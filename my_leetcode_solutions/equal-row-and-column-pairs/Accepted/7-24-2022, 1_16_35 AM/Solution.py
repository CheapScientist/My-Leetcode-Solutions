// https://leetcode.com/problems/equal-row-and-column-pairs

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo1 = defaultdict(set)
        memo2 = defaultdict(set)
        ans = 0
        for r in range(rows):
            temp = ','.join([str(i) for i in grid[r]])
            memo1[temp].add(str(r)+'r')
        for c in range(cols):
            temp = []
            for r in range(rows):
                temp.append(str(grid[r][c]))
            t = ','.join(temp)
            memo2[t].add(str(c)+'c')

        for key in memo1:
            if key in memo2:
                ans += len(memo2[key]) * len(memo1[key])

                
        return ans