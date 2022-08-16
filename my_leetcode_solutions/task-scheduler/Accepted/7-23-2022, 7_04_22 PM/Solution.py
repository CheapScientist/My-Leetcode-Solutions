// https://leetcode.com/problems/task-scheduler

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if n == 0:
            return len(tasks)

        hs = collections.defaultdict(int)
        for task in tasks:
            hs[task] += 1

        count = 0
        cycle = n + 1

        heap = []

        for k in hs:
            if hs[k] > 0:
                heapq.heappush(heap, (-hs[k]))                
        while heap:
            worktime = 0
            tmp = []
            for i in range(cycle):
                if heap:
                    tmp.append(heapq.heappop(heap))
                    worktime += 1
            for cnt in tmp:
                cnt *= -1
                cnt -= 1
                if cnt > 0:
                    heapq.heappush(heap, -cnt)
            
            count += cycle if len(heap) > 0 else worktime

        return count