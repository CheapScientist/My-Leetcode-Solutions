// https://leetcode.com/problems/longest-turbulent-subarray

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if not arr: return -1 
        if len(arr) == 1: return 1
        n = len(arr)
        plus, minus = 1, 1
        res = 1
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