// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        maxStr = ''
        subString = ''
        for i, j in enumerate(s):
            repeatIdx = [ii for ii, ix in enumerate(s) if ix == j]
            if repeatIdx != []:
                for k in repeatIdx:
                    subString = s[i:k+1]
                    if subString == subString[::-1] and len(subString) > maxLen:
                        maxStr = subString
                        maxLen = len(subString)

        return maxStr