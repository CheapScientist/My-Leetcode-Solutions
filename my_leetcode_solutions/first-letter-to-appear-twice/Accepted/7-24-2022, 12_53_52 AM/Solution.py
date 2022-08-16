// https://leetcode.com/problems/first-letter-to-appear-twice

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        v = set()
        for char in s:
            if char not in v:
                v.add(char)
            else:
                return char
        