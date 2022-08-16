// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity

class Solution:
    def largestInteger(self, num: int) -> int:
        evenList, oddList = [], []
        for i, j in enumerate(str(num)):
            if int(j) % 2 == 0:
                evenList.append((i, j))
            else:
                oddList.append((i, j))
        oddList.sort(key = lambda x: x[1], reverse = True)
        evenList.sort(key = lambda x: x[1], reverse = True)
        ans = ''
        even = odd = 0
        for i in range(len(str(num))):
            if int(str(num)[i]) % 2 == 0:
                ans += evenList[even][1]
                even += 1
            else:
                ans += oddList[odd][1]
                odd += 1
        return int(ans)