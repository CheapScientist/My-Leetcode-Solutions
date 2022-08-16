// https://leetcode.com/problems/number-of-digit-one

class Solution:
    def countDigitOne(self, n: int) -> int:
        nList = list(range(1, n + 1))
        strList = []
        for i in nList:
            if '1' in str(i):
                strList.append(str(i))
        totalStr = ''.join(strList)
        count = 0
        for i in totalStr:
            if i == '1':
                count += 1

        return count