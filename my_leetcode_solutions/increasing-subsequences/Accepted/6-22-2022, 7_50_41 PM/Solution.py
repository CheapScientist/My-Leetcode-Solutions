// https://leetcode.com/problems/increasing-subsequences

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1: return []
        dp = [[nums[0]]]
        for i in range(1, len(nums)): 
            num = nums[i]
            for j in range(len(dp)):
                d = dp[j]
                if num >= d[-1]: 
                    dp.append(d + [num])
            dp.append([nums[i]])
        ans = set()
        for d in dp: 
            if len(d) > 1: 
                ans.add(",".join([str(i) for i in d]))
        return [i.split(",") for i in ans]
            