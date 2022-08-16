// https://leetcode.com/problems/repeated-string-match

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        multi = len(b)//len(a)
        for _ in range(3):
            if b in a*multi:
                return multi
            multi += 1
        return -1