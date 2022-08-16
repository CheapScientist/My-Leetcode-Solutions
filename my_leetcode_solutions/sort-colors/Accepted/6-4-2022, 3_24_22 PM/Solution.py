// https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) > 1:
            mi = len(nums) // 2
            leftHalf = nums[:mi]
            rightHalf = nums[mi:]
            self.sortColors(leftHalf)
            self.sortColors(rightHalf)

            # after the above codes the two halves should be sorted already, the rest is to modify the original arr to be
            # sorted
            i = j = k = 0
            while i < len(leftHalf) or j < len(rightHalf):
                left = leftHalf[i] if i < len(leftHalf) else float('inf')
                right = rightHalf[j] if j < len(rightHalf) else float('inf')
                if left < right:
                    nums[k] = leftHalf[i]
                    i += 1
                else:
                    nums[k] = rightHalf[j]
                    j += 1
                k += 1