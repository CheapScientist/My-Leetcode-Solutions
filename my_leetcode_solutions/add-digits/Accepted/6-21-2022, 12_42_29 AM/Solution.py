// https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num: int) -> int:
        
        def helper(s: str) -> int:
            temp = 0
            for i in s:
                temp += int(i)
            return temp
        a = str(helper(str(num)))
        while len(a) > 1:
            num = helper(str(num))
            a = str(helper(str(num)))
        return int(a)