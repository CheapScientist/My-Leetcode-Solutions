// https://leetcode.com/problems/largest-3-same-digit-number-in-string

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if len(num) == 3:
            return num if len(set(num)) == 1 else ''
        res = '000'
        found = False
        i, j = 0, 2
        while j < len(num):
            if len(set(num[i:j+1])) == 1:
                found = True
                if num[i:j+1] > res:
                    res = num[i:j+1]
            i += 1
            j += 1
        return res if found else ''