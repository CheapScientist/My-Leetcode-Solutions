// https://leetcode.com/problems/count-and-say

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        count = 1
        baseStr = '1'
        while count < n:
            baseStr = self.sayStr(baseStr)
            count += 1
        return baseStr


    def sayStr(self, say:str):
        outStr = ''
        prev = say[0]
        count = 1
        for i in range(1, len(say)):
            if say[i] == prev:
                count += 1
            else:
                outStr += str(count) + prev
                prev = say[i]
                count = 1

        outStr += str(count) + say[-1]
        return outStr
        