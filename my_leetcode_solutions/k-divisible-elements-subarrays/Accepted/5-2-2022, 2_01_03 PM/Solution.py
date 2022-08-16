// https://leetcode.com/problems/k-divisible-elements-subarrays

class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int):
        l = len(nums)
        ans = set()
        
        for i in range(l):
            temp = ''
            tempk = 0
            for j in range(i, l):
                if nums[j]%p == 0:
                    tempk += 1
                temp += str(nums[j]) + ','
                if tempk > k:
                    break
                ans.add(temp)

        return len(ans)