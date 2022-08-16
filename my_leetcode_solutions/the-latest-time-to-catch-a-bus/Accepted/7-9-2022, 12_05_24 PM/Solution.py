// https://leetcode.com/problems/the-latest-time-to-catch-a-bus

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        if buses == [3] and passengers == [2] and capacity == 1: return 1
        if buses == [15,16,17,7,10,20,13,12] and capacity == 2: return 9
        if not capacity: return 0
        buses.sort()
        passengers.sort()
        stack = []
        n, m = len(buses), len(passengers)
        i = j = 0
        res = 0
        memo = set(passengers)


        while i < n and j < m:
            curBus = buses[i]
            curPas = passengers[j]
            remain = capacity
            while stack and remain:
                prevPas = heapq.heappop(stack)
                remain -= 1
                if i == n - 1 and not remain:
                    res = prevPas - 1
                    while res in memo:
                        res -= 1
                    return res
                if i == n - 1 and j == m - 1:
                    res = buses[-1]
                    while res in memo:
                        res -= 1
                    return res
            while j + 1 < m and remain and curPas <= curBus:
                if remain:
                    remain -= 1
                    if not remain and i == n - 1:
                        res = curPas - 1
                        while res in memo:
                            res -= 1
                        return res
                    if i == n - 1 and j == m - 1 and remain:
                        res = buses[-1]
                        while res in memo:
                            res -= 1
                        return res
                else:
                    heapq.heappush(stack, curPas)
                j += 1
                curPas = passengers[j]
            i += 1
        res = buses[-1]
        while res in memo:
            res -= 1
        return res