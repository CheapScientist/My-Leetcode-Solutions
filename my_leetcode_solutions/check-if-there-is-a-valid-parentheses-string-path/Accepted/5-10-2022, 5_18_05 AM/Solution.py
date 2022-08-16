// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path

class Solution:
    def hasValidPath(self, A: list[list[str]]) -> bool:
        m, n = len(A), len(A[0])
        dp = defaultdict(set)
        dp[0, -1] = dp[-1, 0] = {0}
        for i in range(m):
            for j in range(n):
                d = 1 if A[i][j] == '(' else -1
                dp[i,j] |= {a + d for a in dp[i-1,j] | dp[i,j-1] if a + d >= 0}
        return 0 in dp[m - 1, n - 1]