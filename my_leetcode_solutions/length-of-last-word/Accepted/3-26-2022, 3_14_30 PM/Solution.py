// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        foundLastWord = False
        s = s[::-1]
        count = 0
        l = 0
        while count in range(len(s)) and not foundLastWord:
            if s[count] == ' ':
                count += 1
            else:
                foundLastWord = True
        while count in range(len(s)) and foundLastWord:
            if s[count] != ' ':
                count += 1
                l += 1
            else:
                foundLastWord = False
        return l