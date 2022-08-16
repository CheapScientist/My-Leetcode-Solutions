// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        num2Letter = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        l = len(digits)
        if l == 0:
            return res
        if l == 1:
            return list(num2Letter[digits[0]])
        if l == 2:
            for i in num2Letter[digits[0]]:
                for j in num2Letter[digits[1]]:
                    res.append(i+j)
        if l == 3:
            for i in num2Letter[digits[0]]:
                for j in num2Letter[digits[1]]:
                    for k in num2Letter[digits[2]]:
                        res.append(i+j+k)
        if l == 4:
            for i in num2Letter[digits[0]]:
                for j in num2Letter[digits[1]]:
                    for k in num2Letter[digits[2]]:
                        for m in num2Letter[digits[3]]:
                            res.append(i+j+k+m)
        return res