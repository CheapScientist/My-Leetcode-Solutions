// https://leetcode.com/problems/01-matrix

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        if not mat: return [[]]
        rows, cols = len(mat), len(mat[0])
        dp = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] != 0:
                    dp[r][c] = -1
        # initialize bfs
        q = deque()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def helper(r, c):
            for direction in directions:
                dr, dc = direction
                newr, newc = r + dr, c + dc
                if helper2(newr, newc) and mat[newr][newc] == 0:
                    return True
            return False

        def helper2(r, c):
            if ((not rows > r >= 0) or
                    (not cols > c >= 0)):
                return False
            return True

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 and helper(r, c):
                    q.append((r, c))
                    mat[r][c] = -1
                    dp[r][c] = 1
        curDist = 2
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for direction in directions:
                    dr, dc = direction
                    newr, newc = r + dr, c + dc
                    if (helper2(newr, newc) and
                            mat[newr][newc] == 1):
                        q.append((newr, newc))
                        mat[newr][newc] = -1
                        dp[newr][newc] = curDist
            curDist += 1
        return dp