// https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = len(s)
        a = 2 * numRows - 2
        if a == 0:
            return s
        nofIterations = l // a
        iterationStart = 0
        outStr = [''] * numRows
        fs = ''
        if l <= a:
            for j in range(l):
                idx = j
                if j < numRows:
                    outStr[j] += s[j]
                else:
                    outStr[a - j] += s[j]
                print(outStr)
            for k in outStr:
                fs += k
            return fs
        for i in range(nofIterations):
            for j in range(a):
                idx = j + (a)*iterationStart
                if j < numRows:
                    outStr[j] += s[idx]
                else:
                    outStr[a - j] += s[idx]
                print(outStr)
            iterationStart += 1
        for k in range(l - l%a, l):
            idx = k%a
            if idx < numRows:
                outStr[idx] += s[k]
            else:
                outStr[a-idx] += s[k]
        for i in outStr:
            fs += i
        return fs