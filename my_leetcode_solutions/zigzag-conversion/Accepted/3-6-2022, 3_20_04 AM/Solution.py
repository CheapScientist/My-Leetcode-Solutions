// https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l  = len(s)
        a = 2*numRows - 2
        outStr = ['']*numRows
        fs = ''
        for idx in range(l):
            if a == 0:
                return s
            i = idx%a
            outStr[min(i%a, (a-i)%a)] += s[idx]
        for i in outStr:
            fs += i
        return fs