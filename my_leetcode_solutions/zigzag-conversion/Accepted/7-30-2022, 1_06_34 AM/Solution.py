// https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        div = numRows + (numRows - 2)
        for i in range(len(s)):
            if numRows > i%div >=0:
                res[i%div].append(s[i])
            else:
                res[div - i%div].append(s[i])
        ans = []
        for i in res:
            for j in i:
                ans.append(j)
        return ''.join(ans)