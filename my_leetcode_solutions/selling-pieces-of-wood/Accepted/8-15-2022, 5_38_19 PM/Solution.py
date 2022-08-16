// https://leetcode.com/problems/selling-pieces-of-wood

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for h, w, p in prices:
            f[h][w] = p
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = max(f[i][j],
                              max((f[i][k] + f[i][j - k] for k in range(1, j // 2 + 1)), default=0),  # 垂直切割
                              max((f[k][j] + f[i - k][j] for k in range(1, i // 2 + 1)), default=0))  # 水平切割
        return f[m][n]
