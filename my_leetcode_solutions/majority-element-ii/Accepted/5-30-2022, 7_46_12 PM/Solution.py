// https://leetcode.com/problems/majority-element-ii

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums)//3
        res = []
        memo = {}
        for num in nums:
            memo[num] = 1 + memo.get(num, 0)
        for i in memo:
            if memo[i] > target:
                res.append(i)
        return res