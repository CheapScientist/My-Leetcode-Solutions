// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        num2Letter = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", 
                      '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = []
        
        def dfs(i, cur):
            if i == len(digits):
                res.append(cur)
                return 
            
            for n in num2Letter[digits[i]]:
                dfs(i + 1, cur + n)
        dfs(0, '')
        return res