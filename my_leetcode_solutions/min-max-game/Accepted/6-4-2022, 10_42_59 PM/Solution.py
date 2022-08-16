// https://leetcode.com/problems/min-max-game

class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def recursive(nums):
            if len(nums) == 1:
                return nums
            l, r = 0, len(nums) - 1
            mi = (l + r) // 2
            left, right = nums[:mi + 1], nums[mi + 1:]
            newNums = []
            for i in range(mi + 1):
                if i % 2 == 0:
                    newNums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    newNums.append(max(nums[2 * i], nums[2 * i + 1]))
            return recursive(newNums)

        return recursive(nums)[0]