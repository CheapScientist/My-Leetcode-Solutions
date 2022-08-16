// https://leetcode.com/problems/delete-operation-for-two-strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)

        dp = [i for i in range(cols + 1)]
        for r in range(1, rows + 1):
            temp = [r] * (cols + 1)
            for c in range(1, cols + 1):
                if word1[r - 1] == word2[c - 1]:
                    temp[c] = dp[c - 1]
                else:
                    temp[c] = 1 + min(temp[c - 1], dp[c])
            dp = temp[:]
        return dp[-1]