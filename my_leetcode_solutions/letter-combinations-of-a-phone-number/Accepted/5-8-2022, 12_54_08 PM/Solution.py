// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        for i in digits:
            if i not in '23456789':
                return -1
        num2Letter = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", 
                      '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        res = []
        
        def dfs(i, path): # i indicates which character it's currently working on. path is the string that we are building up
            if len(path) == len(digits):
                res.append(path)
                return
            
            for char in num2Letter[digits[i]]:
                dfs(i + 1, path + char)
        
        dfs(0, '')
        return res