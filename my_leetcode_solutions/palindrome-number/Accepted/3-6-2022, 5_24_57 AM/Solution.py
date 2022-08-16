// https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strX = str(x)
        lenX = len(strX)
        if lenX == 1:
            return True
        if lenX%2 == 0:
            lpointer = lenX//2 - 1
            rpointer = lenX//2
        else:
            lpointer = lenX//2 - 1
            rpointer = lenX//2 + 1
        while lpointer in range(lenX) and rpointer in range(lenX):
            print(strX[lpointer], strX[rpointer])
            if strX[lpointer] != strX[rpointer]:
                return False
            else:
                lpointer -= 1
                rpointer += 1
        return True
