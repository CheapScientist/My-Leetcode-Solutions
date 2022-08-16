// https://leetcode.com/problems/nim-game

class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 3:
            return True
        if (n - 3)%4 == 1:
            return False
        else:
            return True