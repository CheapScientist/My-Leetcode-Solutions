// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2Letter = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        if digits == '':
            return []
        res = ['']
        for i in digits:
            temp = []
            for j in res:
                for k in num2Letter[i]:
                    temp.append(j + k)
            res = temp
        return res