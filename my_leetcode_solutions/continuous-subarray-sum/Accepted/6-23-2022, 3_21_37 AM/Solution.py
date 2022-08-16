// https://leetcode.com/problems/continuous-subarray-sum

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref = {0: -1}
        total = 0
        for i, j in enumerate(nums):
            total += j
            r = total%k
            if r not in pref: 
                pref[r] = i
            elif i - pref[r] > 1:
                return True
            
        return False