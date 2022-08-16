// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        @cache
        def dfs(i): 
            if i == n: return True
            for j in range(i, n): 
                if s[i:j + 1] in wordSet:
                    if dfs(j + 1): return True
            return False
        
        return dfs(0)