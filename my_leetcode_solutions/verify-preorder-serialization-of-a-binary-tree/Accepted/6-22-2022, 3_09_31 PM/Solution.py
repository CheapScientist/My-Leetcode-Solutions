// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        newList = preorder.split(',')
        stack = []
        
        for i in newList:
            stack.append(i)
            if i == '#': 
                while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append('#')
        return True if stack == ['#'] else False
                        
                        
        
        