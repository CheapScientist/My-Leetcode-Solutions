// https://leetcode.com/problems/4sum

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for start_pointer1 in range(len(nums)-3):
            for start_pointer2 in range(start_pointer1 + 1, len(nums)-2):
                l_pointer = start_pointer2 + 1
                r_pointer = len(nums) - 1
                while l_pointer < r_pointer:
                    fsum = nums[start_pointer1] + nums[start_pointer2] + nums[l_pointer] +nums[r_pointer]
                    if fsum > target:
                        r_pointer -= 1
                    elif fsum == target:
                        if [nums[start_pointer1], nums[start_pointer2], nums[l_pointer], nums[r_pointer]] not in res:
                            res.append([nums[start_pointer1], nums[start_pointer2], nums[l_pointer], nums[r_pointer]])
                        l_pointer += 1
                        r_pointer -= 1
                    else:
                        l_pointer += 1
        return res