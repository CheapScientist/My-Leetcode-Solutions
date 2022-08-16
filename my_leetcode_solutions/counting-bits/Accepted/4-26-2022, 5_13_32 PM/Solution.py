// https://leetcode.com/problems/counting-bits

class Solution:
    def countBits(self, n: int) -> List[int]:
        if not n: return [0]
        ans = []
        for i in range(n + 1):
            temp = 0
            while i:
                temp += i % 2
                i = i//2
            ans.append(temp)
        return ans