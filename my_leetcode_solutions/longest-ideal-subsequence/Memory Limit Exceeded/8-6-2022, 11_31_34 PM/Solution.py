// https://leetcode.com/problems/longest-ideal-subsequence

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        A = [ord(i) - ord('a') for i in s]
        n = len(A)

        @cache
        def dfs(i, prev):
            if i == n:
                return 0
            if abs(A[i] - prev) <= k:
                return max(dfs(i + 1, prev), 1 + dfs(i + 1, A[i]))
            return dfs(i + 1, prev)
        return max([dfs(i, A[i]) for i in range(n)])