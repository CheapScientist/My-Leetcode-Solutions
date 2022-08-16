// https://leetcode.com/problems/permutation-in-string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1lookup = {}
        for i in s1:
            if i in s1lookup:
                s1lookup[i] += 1
            else:
                s1lookup[i] = 1
        l, s1length = 0, len(s1)
        while l + s1length - 1 in range(len(s2)):
            temp = s1lookup.copy()
            s2sliderStr = s2[l: l + s1length]
            found = True
            for j in s2sliderStr:
                if j not in temp or temp[j] == 0:
                    break
                else:
                    temp[j] -= 1
            for k in temp.values():
                if k != 0:
                    found = False 
                    break
            if found:
                return True
            l += 1
        return False