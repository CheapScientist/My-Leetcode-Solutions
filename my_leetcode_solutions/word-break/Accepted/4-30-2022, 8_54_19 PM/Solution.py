// https://leetcode.com/problems/word-break

class Solution:
    
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word = set(wordDict)
        l = len(s)
        @lru_cache
        def dfs(start):
            if start >= l:
                return True
            for i in range(start, l):
                if s[start:i+1] in word:
                    if dfs(i + 1):
                        return True
            return False
        return dfs(0)