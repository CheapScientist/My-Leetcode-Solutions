// https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for i in preorder.split(','):
            if i != "#": 
                stack.append(i)
            else:
                if stack and stack[-1] != "#":
                    stack.append("#")
                    continue
                stack.append("#")
                while len(stack) > 2 and stack[-1] == '#' and stack[-2] == '#' and stack[-3] != "#":
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append("#")
        # print(stack)

        return True if stack == ["#"] else False