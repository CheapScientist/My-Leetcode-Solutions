// https://leetcode.com/problems/longest-string-chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        lookup = set(words)
        @cache
        def dfs(word):
            if word not in lookup:
                return 0
            m = len(word)
            return max(1 + dfs(word[:i]+word[i+1:]) for i in range(m))
        words.sort(key = lambda x: -len(x))
        return max(dfs(words[i]) for i in range(n))