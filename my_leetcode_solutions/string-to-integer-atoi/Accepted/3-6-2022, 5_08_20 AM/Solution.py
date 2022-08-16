// https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        ss = s.strip()
        finalStr = ''
        numlist = []
        sign = 1
        for i in range(10):
            numlist.append(str(i))
        if not ss:
            return 0

        if ss[0] == '+':
            sign = 1
        elif ss[0] == '-':
            sign = -1
        elif ss[0] not in numlist:
            return 0
        elif ss[0] in numlist:
            finalStr += ss[0]
        for i in range(1, len(ss)):
            if ss[i] in numlist:
                finalStr += ss[i]
            else:
                break
        if not finalStr:
            return 0
        res = int(finalStr)*sign
        if res < -2 ** (31):
            res = -2 ** (31)
        elif res >= 2 ** (31):
            res = 2 ** (31) - 1
        return res
