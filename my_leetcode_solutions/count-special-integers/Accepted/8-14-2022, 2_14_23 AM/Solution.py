// https://leetcode.com/problems/count-special-integers

class Solution:
    def countSpecialNumbers(self, N: int) -> int:
        L = list(map(int, str(N + 1)))
        res, n = 0, len(L)

        def A(m, n):
            res = 1
            for i in range(n):
                res *= m
                m -= 1
            return res
        for i in range(1, n): res += 9 * A(9, i - 1)
        s = set()
        for i, x in enumerate(L):
            for y in range(not i, x):
                if y not in s:
                    res += A(9 - i, n - i - 1)
            if x in s: break
            s.add(x)
        return res
        