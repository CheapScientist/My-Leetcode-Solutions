// https://leetcode.com/problems/dungeon-game

class Solution:
    def calculateMinimumHP(self, dungeon):
        if not dungeon: return -1
        rows, cols = len(dungeon), len(dungeon[0])
        matrix = dungeon
        dp = [[0] * cols for i in range(rows)]
        if matrix[-1][-1] <= 0:
            dp[-1][-1] = 1 - matrix[-1][-1]
        else:
            dp[-1][-1] = 1
        for j in range(cols - 1, -1, -1):
            for i in range(rows - 1, -1, -1):
                if [i, j] != [rows - 1, cols - 1]:
                    a1 = dp[i][j + 1] if cols > j + 1 >= 0 else float('inf')
                    a2 = dp[i + 1][j] if rows > i + 1 >= 0 else float('inf')
                    dp[i][j] = min(a1, a2) - matrix[i][j] if min(a1, a2) > matrix[i][j] else 1

        return dp[0][0] if dp[0][0] != float('inf') else 1