// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word = set(wordDict)
        l = len(s)
        memo = {}

        def dfs(start):
            if start >= l:
                return True
            if start in memo:
                return memo[start]
            for i in range(start, l):
                if s[start:i+1] in word:
                    if dfs(i + 1):
                        memo[start] = True
                        return True
            memo[start] = False
            return False
        return dfs(0)