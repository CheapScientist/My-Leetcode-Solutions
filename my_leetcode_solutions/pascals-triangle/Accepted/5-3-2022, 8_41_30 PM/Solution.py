// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # initialize data set:
        ans = []
        for i in range(1, numRows + 1):
            ans.append([0]*i)
        for i in ans:
            i[0], i[-1] = 1, 1
        if numRows < 2:
            return ans
        for i in range(2, numRows + 1):
            for j in range(i - 1):
                if ans[i - 1][j] == 0:
                    ans[i - 1][j] = ans[i - 2][j] + ans[i - 2][j - 1]
        return ans