// https://leetcode.com/problems/find-common-characters

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = [[0]*26 for _ in range(len(words))]
        for idx, word in enumerate(words):
            for char in word:
                ans[idx][ord(char) - ord('a')] += 1
        res = []
        for i in range(26):
            mn = len(words)
            for j in range(len(ans)):
                mn = min(mn, ans[j][i])
            if mn:
                res.extend(list(mn*chr(ord('a') + i)))
        return res
        