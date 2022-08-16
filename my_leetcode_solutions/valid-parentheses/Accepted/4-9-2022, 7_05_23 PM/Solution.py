// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        ansStack = []
        parentDict = {')': '(', ']':'[', '}':'{'}
        for i in s:
            if i in '([{':
                ansStack.append(i)
            elif i in ')}]':
                if len(ansStack) == 0:
                    return False
                else:
                    if ansStack[-1] == parentDict[i]:
                        ansStack.pop()
                    else:
                        return False
            else:
                return False
        return True if ansStack == [] else False
        