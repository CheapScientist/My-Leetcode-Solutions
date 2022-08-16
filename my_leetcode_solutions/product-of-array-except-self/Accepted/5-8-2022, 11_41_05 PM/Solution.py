// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        if not a: return []
        if len(a) == 1: return a
        p = 1
        n = len(a)
        output = []
        for i in range(n):
            output.append(p)
            p = p * a[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * a[i]
        return output