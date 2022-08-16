// https://leetcode.com/problems/3sum-closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        smallestDiff = float('inf')
        res = 0
        nums.sort()
        for start_pointer in range(len(nums) - 2):
            if start_pointer >= 1 and nums[start_pointer] == nums[start_pointer - 1]:
                continue
            l_pointer = start_pointer + 1
            r_pointer = len(nums) - 1
            while r_pointer > l_pointer:
                tsum = nums[l_pointer] + nums[r_pointer] + nums[start_pointer]
                localDiff = abs(target - tsum)
                if localDiff < smallestDiff:
                    smallestDiff = localDiff
                    res = tsum
                if tsum > target:
                    while r_pointer - 1 > l_pointer and nums[r_pointer] == nums[r_pointer - 1]:
                        r_pointer -= 1
                    r_pointer -= 1
                else:
                    while l_pointer + 1 < r_pointer and nums[l_pointer] == nums[l_pointer + 1]:
                        l_pointer += 1
                    l_pointer += 1
        return res