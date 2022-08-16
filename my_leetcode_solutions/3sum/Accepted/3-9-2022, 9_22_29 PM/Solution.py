// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for start_pointer in range(len(nums) - 2):
            if start_pointer >= 1 and nums[start_pointer] == nums[start_pointer - 1]:
                continue
            if nums[start_pointer] > 0:
                break
            l_pointer = start_pointer + 1
            r_pointer = len(nums) - 1
            while r_pointer > l_pointer:
                tsum = nums[l_pointer] + nums[r_pointer] + nums[start_pointer]
                if tsum > 0:
                    r_pointer -= 1
                elif tsum == 0:
                    res.append([nums[l_pointer], nums[r_pointer], nums[start_pointer]])
                    l_pointer += 1
                    while nums[l_pointer] == nums[l_pointer - 1] and l_pointer < r_pointer:
                        l_pointer += 1
                else:
                    l_pointer += 1
        return res