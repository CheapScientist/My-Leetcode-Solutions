// https://leetcode.com/problems/word-break

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        if len(s) == 1: return s in wordDict
        dp = [False] * (len(s)+1)
        dp[-1] = True
        word = set(wordDict)
        for i in range(len(s) - 1, -1, -1):
            temp = []
            for j in range(i + 1, len(s)+1):
                if dp[j]:
                    temp.append(j)

            for k in temp:
                if s[i:k] in word:
                    dp[i] = True
                    break
        return dp[0]