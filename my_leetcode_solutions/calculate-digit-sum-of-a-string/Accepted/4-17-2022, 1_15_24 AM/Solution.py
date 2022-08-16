// https://leetcode.com/problems/calculate-digit-sum-of-a-string

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def rp(s: str):
            res = 0
            for i in s:
                res += int(i)
            return str(res)
        while len(s) > k:
            temp = ''
            for i in range(0, len(s), k):
                if i + k in range(len(s)):
                    ans = rp(s[i:i+k])
                else:
                    ans = rp(s[i:])
                temp += ans
            s = temp
        return s