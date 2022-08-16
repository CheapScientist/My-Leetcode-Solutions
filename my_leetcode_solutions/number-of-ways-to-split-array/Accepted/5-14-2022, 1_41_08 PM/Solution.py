// https://leetcode.com/problems/number-of-ways-to-split-array

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixSum = []
        postfixSum = []
        for i in nums:
            a1 = prefixSum[-1] if prefixSum else 0
            prefixSum.append(a1 + i)
        for i in range(len(nums) - 1, -1, -1):
            a1 = postfixSum[-1] if postfixSum else 0
            postfixSum.append(a1 + nums[i])
        postfixSum = postfixSum[::-1]
        ans = 0
        for i in range(len(nums) - 1):
            if prefixSum[i] >= postfixSum[i + 1]:
                ans += 1
        return ans
        
        