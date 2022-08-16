// https://leetcode.com/problems/calculate-amount-paid-in-taxes

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        remain = income
        res = 0
        u, p = brackets[0]
        if remain > u: 
            res += u*p/100
        else:
            res += remain*p/100
            return res
        if len(brackets) == 1: 
            return res
        for i in range(1, len(brackets)): 
            u, p = brackets[i]
            prevu = brackets[i - 1][0]
            if remain > u: 
                res += (u - prevu)*p/100
            else:
                res += (remain - prevu) * p/100
                break
        return res