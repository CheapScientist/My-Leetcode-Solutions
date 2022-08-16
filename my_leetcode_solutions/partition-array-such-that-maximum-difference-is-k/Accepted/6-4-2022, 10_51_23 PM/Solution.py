// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1
        nums.sort()
        
        ans = 0 
        l, r = 0, 0
        # res = []
        while r < len(nums):
            prev = nums[l]
            while r + 1 < len(nums) and nums[r + 1] - prev <= k: 
                r += 1
            # res.append(nums[l:r + 1])
            ans += 1
            l = r + 1
            r += 1
        return ans
            