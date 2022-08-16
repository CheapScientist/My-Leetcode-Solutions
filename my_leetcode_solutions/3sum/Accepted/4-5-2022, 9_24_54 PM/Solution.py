// https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        cp, res = sorted(nums), []
        i = 0
        while i in range(len(cp) - 2):
            ans = self.twoSum(cp, i + 1, len(cp) - 1, -cp[i])
            for k in ans:
                res.append(k + [cp[i]])
            i += 1
            while i in range(len(cp)) and cp[i-1] == cp[i]:
                i += 1

        return res

    def twoSum(self, numbers, l, r, target: int):
        ans = []
        while l < r:
            if numbers[l] + numbers[r] == target:
                ans.append([numbers[l], numbers[r]])
                l += 1
                while numbers[l] == numbers[l - 1] and l < r:
                    l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return ans