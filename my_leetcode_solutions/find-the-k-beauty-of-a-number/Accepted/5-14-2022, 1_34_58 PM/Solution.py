// https://leetcode.com/problems/find-the-k-beauty-of-a-number

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        if not k: return 0
        ans = 0
        nums = str(num)
        for i in range(len(nums) - k + 1):
            a = int(nums[i:i+k])
            if a and num%a == 0:
                ans += 1
        return ans
        
        