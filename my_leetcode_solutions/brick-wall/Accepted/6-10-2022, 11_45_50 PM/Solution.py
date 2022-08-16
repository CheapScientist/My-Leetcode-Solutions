// https://leetcode.com/problems/brick-wall

class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        rows, lines = len(wall), sum(wall[0])
        dp = {0:0}
        for r in range(rows):
            temp = 0
            for c in range(len(wall[r]) - 1):
                temp += wall[r][c]
                dp[temp] = dp.get(temp, 0) + 1
        return len(wall) - max(dp.values())