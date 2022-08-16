// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
             return False 
        hashM = {}
        for i in s:
            if i in hashM:
                hashM[i] += 1
            else:
                hashM[i] = 1
        for j in t:
            if j in hashM:
                if hashM[j] == 0:
                    return False
                else:
                    hashM[j] -= 1
            else:
                return False
        return True
        