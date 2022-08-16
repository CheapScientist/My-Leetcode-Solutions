// https://leetcode.com/problems/insert-interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newstart, newend = newInterval
        res = []
        
        for idx, interval in enumerate(intervals): 
            start, end = interval
            if start > newend: 
                res.append([newstart, newend])
                return res + intervals[idx:]
            elif newstart > end: 
                res.append(interval)
            else:
                newstart, newend = min(start, newstart), max(end, newend)
        res.append([newstart, newend])
        return res