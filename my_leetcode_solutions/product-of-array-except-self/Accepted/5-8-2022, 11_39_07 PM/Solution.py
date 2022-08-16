// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        if not a: return []
        if len(a) == 1: return a
        left, right = [1], [1]
        l, r = 1, 1
        for i in range(1, len(a)):
            l *= a[i - 1]
            left.append(l)
        for i in range(len(a) - 2, -1, -1):
            r *= a[i + 1]
            right.append(r)
        # print (left, right)
        res = []
        right = right[::-1]
        for i in range(len(a)):
            res.append(left[i] * right[i])
        return res