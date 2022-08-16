// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 0: return 0
        if len(tokens) == 1: return int(tokens[0])
        ansStack = []
        res = 0
        for i in tokens:
            if i in '/*-+':
                val1 = int(ansStack.pop())
                val2 = int(ansStack.pop())
                if i == '/':
                    res = val2 / val1
                    res = int(res)
                elif i == '*':
                    res = val2 * val1
                elif i == '-':
                    res = val2 - val1
                else:
                    res = val2 + val1

                ansStack.append(res)
            else:
                ansStack.append(int(i))
        return res