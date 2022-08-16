// https://leetcode.com/problems/minimum-time-difference

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) == 1: return -1
        minuteList = []
        
        def helper(s): 
            l = s.split(':')
            temp = int(l[0])*60 + int(l[1])
            return temp
        for i in range(len(timePoints)):
            minuteList.append(helper(timePoints[i]))
        
        minuteList.sort()
        res = float('inf')
        for i in range(1, len(minuteList)):
            res = min(res, minuteList[i] - minuteList[i - 1])
        return min(res, 1440 - abs(minuteList[0] - minuteList[-1]))