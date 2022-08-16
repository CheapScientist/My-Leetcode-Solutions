// https://leetcode.com/problems/remove-k-digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = k
        finish = False
        for i in num:
            if not finish:
                if not stack:
                    stack.append(i)
                else:
                    while stack and stack[-1] > i and remain:
                        stack.pop()
                        remain -= 1
                        if remain == 0:
                            finish = True
                    stack.append(i)
            else:
                stack.append(i)
        # print(remain ,stack)
        while remain:
            stack.pop()
            remain -= 1
        return str(int(''.join(stack))) if stack else "0"
                        
        