// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        if not maze: return -1
        rows, cols = len(maze), len(maze[0])
        q = deque([entrance])
        ans = 0
        visit = set(tuple(entrance))
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def check(x, y):
            if [x, y] == entrance:
                return False
            if maze[x][y] == '.':
                if (x == 0 or x == rows - 1) or (y == 0 or y == cols - 1):
                    return True
            return False

        while q:
            for _ in range(len(q)):
                A = q.popleft()
                curx, cury = A
                if check(curx, cury):
                    return ans

                for direction in directions:
                    dx, dy = direction
                    if (curx + dx, cury + dy) not in visit and (rows > curx + dx >= 0 and cols > cury + dy >= 0) and maze[curx + dx][cury + dy] == '.':
                        visit.add((curx + dx, cury + dy))
                        q.append((curx + dx, cury + dy))
            ans += 1
        return -1