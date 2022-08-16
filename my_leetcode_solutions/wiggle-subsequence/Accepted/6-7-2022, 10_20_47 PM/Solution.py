// https://leetcode.com/problems/wiggle-subsequence

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        if len(nums) == 2: return 2 if nums[0] != nums[1] else 1
        diff = [0]
        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i - 1])
        dp = [0]*len(nums)
        dp[0] = 1
        dp[1] = 2 if nums[0] != nums[1] else 1
        ans = max(dp[0], dp[1])
        for i in range(2, len(nums)):
            temp = 0
            # case 1: diff is 0 for this index, dp[i] is 0 
            if diff[i] == 0:
                dp[i] = 1
            else:
                for j in range(i): 
                    if diff[i]*diff[j] < 0 or not diff[j]:
                        temp = max(temp, 1 + dp[j])
                    else:
                        temp = max(temp, 1)
                dp[i] = temp
            ans = max(dp[i], ans)
        print(diff, dp)
        return ans
        