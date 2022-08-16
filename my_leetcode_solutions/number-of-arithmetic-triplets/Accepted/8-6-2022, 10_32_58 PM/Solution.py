// https://leetcode.com/problems/number-of-arithmetic-triplets

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] - nums[i] > diff:
                    break
                if nums[j] - nums[i] < diff:
                    continue
                for k in range(j + 1, n):
                    if nums[k] - nums[j] > diff:
                        break
                    if nums[k] - nums[j] < diff:
                        continue
                    ans += 1
                    
        return ans
                    