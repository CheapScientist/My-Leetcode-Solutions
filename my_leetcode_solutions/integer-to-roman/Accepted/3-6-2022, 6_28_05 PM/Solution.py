// https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        numStr = str(num)
        romanList = ['IV', 'XL', 'CD', 'M']
        romanStr = ''
        ## 2. see how long the number is. For example if the length is 1, check the first two elements(2*1), if the length is 2 check the first 4
        # start from the first element. i.e if the number is 38, first number is 3, less than 4, so it is assigned with XXX
        l = len(numStr)
        for i, j in enumerate(numStr):
            r = romanList[l - 1]
            if int(j) < 4:
                romanStr += r[0]*int(j)
            elif int(j) == 4:
                romanStr += r
            elif int(j) <= 8:
                romanStr += r[1] + r[0]*(int(j) - 5)
            else:
                r2 = romanList[l]
                romanStr += r[0]+r2[0]
            l -= 1
        return romanStr