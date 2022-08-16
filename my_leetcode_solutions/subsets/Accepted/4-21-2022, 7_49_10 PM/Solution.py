// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: list[int]):
        temp = [[]]
        while nums:
            cur = nums.pop(0)
            for i in range(len(temp)):
                x = temp.pop(0)
                temp.append(x + [cur])
                temp.append(x)
        return temp