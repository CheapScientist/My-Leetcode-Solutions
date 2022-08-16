// https://leetcode.com/problems/task-scheduler-ii

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        last = {}
        for task in tasks:
            day += 1
            if task in last:
                day = max(day, last[task] + space + 1)
            last[task] = day
        return day