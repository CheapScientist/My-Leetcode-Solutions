// https://leetcode.com/problems/count-hills-and-valleys-in-an-array

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        newL = []
        newL.append(nums[0])
        prev = nums[0]
        for cur in nums[1:]:
            if cur != prev:
                newL.append(cur)
                prev = cur
        ans = 0
        for i in range(1, len(newL) - 1):
            if newL[i-1] > newL[i] and newL[i] < newL[i+1]:
                ans += 1
            elif newL[i-1] < newL[i] and newL[i] > newL[i+1]:
                ans += 1
        return ans