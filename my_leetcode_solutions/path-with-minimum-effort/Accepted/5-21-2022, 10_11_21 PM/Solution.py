// https://leetcode.com/problems/path-with-minimum-effort

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # sanity check
        if not heights: return -2
        rows, cols = len(heights), len(heights[0])
        minH = [(0, 0, 0)]  #weight, r, c
        visit = set()

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        while minH: 
            curW, curR, curC = heapq.heappop(minH)
            if (curR, curC) in visit: 
                continue
            visit.add((curR, curC))
            if (curR, curC) == (rows - 1, cols - 1):
                return curW
            for dr, dc in directions:
                newR, newC = dr + curR, dc + curC
                if (rows > newR >= 0 and cols > newC >= 0): 
                    a1 = max(curW, abs(heights[newR][newC] - heights[curR][curC]))
                    heappush(minH, [a1, newR, newC])  # max(abs(prev - cur), abs(delta heights)), r, c
        return -1