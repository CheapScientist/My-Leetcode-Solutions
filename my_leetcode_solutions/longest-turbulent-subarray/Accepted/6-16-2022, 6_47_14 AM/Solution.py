// https://leetcode.com/problems/longest-turbulent-subarray

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr: return -1 
        if len(arr) == 1: return 1
        n = len(arr)
        dp = [[1]*n for _ in range(2)]
        res = 1
        # e.g: arr = [9,4,2,10,7,8,8,1,9]
        #           [[1,1,1,3,1,5,1,2], first row is positive subarray 
        #            [1,2,2,1,4,1,1,1]] second row is negative subarray
        # if nums[i] == nums[i - 1]: dp[i][0] = dp[i][1] = 1, or continue
        # if nums[i] > nums[i - 1]: dp[i][0] = dp[i - 1][1] + 1
        # if nums[i] < nums[i - 1]: dp[i][1] = dp[i - 1][0] + 1
        for i in range(1, n):
            if arr[i] == arr[i - 1]: 
                continue
            elif arr[i] > arr[i - 1]: 
                dp[0][i] = dp[1][i - 1] + 1
            else:
                dp[1][i] = dp[0][i - 1] + 1
            res = max(res, dp[1][i], dp[0][i])

        return res