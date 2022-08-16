// https://leetcode.com/problems/word-break-ii

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        lookup = set()
        mn = float('inf')
        for word in wordDict:
            lookup.add(word)
            mn = min(mn, len(word))
        ans = []
        build = []

        def dfs(i):
            if i == len(s):
                copy = ' '.join(build)
                ans.append(copy)
                return
            if len(s) - i < mn:
                return
            for j in range(i, len(s)):
                if s[i:j + 1] in lookup:
                    build.append(s[i:j + 1])
                    dfs(j + 1)
                    build.pop()
            return

        dfs(0)
        return ans