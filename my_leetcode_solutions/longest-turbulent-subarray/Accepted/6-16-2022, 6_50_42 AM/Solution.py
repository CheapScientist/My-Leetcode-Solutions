// https://leetcode.com/problems/longest-turbulent-subarray

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr: return -1 
        if len(arr) == 1: return 1
        n = len(arr)
        plus, minus = 1, 1
        res = 1
        # e.g: arr = [9,4,2,10,7,8,8,1,9]
        #           [[1,1,1,3,1,5,1,2], first row is positive subarray 
        #            [1,2,2,1,4,1,1,1]] second row is negative subarray
        # if nums[i] == nums[i - 1]: dp[i][0] = dp[i][1] = 1, or continue
        # if nums[i] > nums[i - 1]: dp[i][0] = dp[i - 1][1] + 1
        # if nums[i] < nums[i - 1]: dp[i][1] = dp[i - 1][0] + 1
        for i in range(1, n):
            if arr[i] == arr[i - 1]: 
                plus, minus = 1, 1
            elif arr[i] > arr[i - 1]: 
                plus = minus + 1
                minus = 1
            else:
                minus = plus + 1
                plus = 1
            res = max(res, plus, minus)
        return res