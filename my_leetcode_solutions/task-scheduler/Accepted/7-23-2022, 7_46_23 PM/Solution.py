// https://leetcode.com/problems/task-scheduler

class Solution(object):
    def leastInterval(self, tasks, n):
        if not n:
            return len(tasks)

        counter = Counter(tasks)
        maxHeap = []
        count, cycle = 0, n + 1
        for key in counter:
            heapq.heappush(maxHeap, -counter[key])
                    
        while maxHeap:
            worktime = 0
            temp = []
            for i in range(cycle):
                if not maxHeap:
                    break
                temp.append(heapq.heappop(maxHeap))
                worktime += 1

            for t in temp:
                t = - t - 1
                if t:
                    heapq.heappush(maxHeap, -t)
            
            count += cycle if len(maxHeap) > 0 else worktime

        return count