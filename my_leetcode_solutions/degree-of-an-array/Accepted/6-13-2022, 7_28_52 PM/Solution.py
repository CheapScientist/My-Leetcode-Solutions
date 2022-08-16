// https://leetcode.com/problems/degree-of-an-array

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        memo = {}
        for i in nums: 
            memo[i] = memo.get(i, 0) + 1
        q = []
        mx = max(memo.values())
        if mx == 1: 
            return 1
        for key in memo: 
            if memo[key] == mx: 
                q.append(key)
        mn = len(nums)
        for candidate in q: 
            for i in range(len(nums)): 
                if nums[i] == candidate: 
                    left = i
                    break
            for i in range(len(nums) - 1, -1 , -1): 
                if nums[i] == candidate: 
                    right = i
                    break
            mn = min(mn, (right - left + 1))
        return mn
        