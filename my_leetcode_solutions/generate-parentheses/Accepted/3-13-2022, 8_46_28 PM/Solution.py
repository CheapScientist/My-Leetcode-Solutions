// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = ['()']
        if n == 1:
            return ans
        ansDict = {}
        for i in range(1, n):
            temp = []
            for j in ans:
                temp += self.insertIntoParenthesis(j, '()')
                ans = temp
        for i in ans:
            if i not in ansDict:
                ansDict[i] = 1
            else:
                ansDict[i] += 1
        finalAns = []
        for i in ansDict:
            finalAns.append(i)
        return finalAns

    def insertIntoParenthesis(self, aStr, insertStr):
        ans = []
        for i in range(len(aStr)):
            ans.append(aStr[:i] + insertStr + aStr[i:])
        return ans