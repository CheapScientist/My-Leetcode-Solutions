// https://leetcode.com/problems/count-square-sum-triples

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if n >= (i**2 + j**2)**0.5 >=1:
                    if int((i**2 + j**2)**0.5)**2 == i**2 + j**2:
                        ans += 1

        return ans