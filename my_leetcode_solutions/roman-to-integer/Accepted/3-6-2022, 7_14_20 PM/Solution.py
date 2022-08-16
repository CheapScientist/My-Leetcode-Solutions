// https://leetcode.com/problems/roman-to-integer

class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        # look for each str in s. if the value of the ith element is smaller than or equal to the second, sum -= romanDict[i]
        l = len(s) - 1
        i = 0
        while i < l:
            if romanDict[s[i]] < romanDict[s[i+1]]:
                sum -= romanDict[s[i]]
            else:
                sum += romanDict[s[i]]
            i += 1
        sum += romanDict[s[-1]]
        return sum
