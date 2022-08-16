// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashM = {}
        duplicate = False
        for i in nums:
            if i in hashM:
                if hashM[i] == 1:
                    duplicate = True
                    return duplicate
            else:
                hashM[i] = 1
        return duplicate