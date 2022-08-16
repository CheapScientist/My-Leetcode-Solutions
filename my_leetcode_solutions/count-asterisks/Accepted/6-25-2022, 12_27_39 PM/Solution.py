// https://leetcode.com/problems/count-asterisks

class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        seenBar = 0
        for char in s: 
            if char == "|":
                seenBar += 1
            if seenBar % 2 == 0 and char == "*":
                ans += 1
        return ans
        