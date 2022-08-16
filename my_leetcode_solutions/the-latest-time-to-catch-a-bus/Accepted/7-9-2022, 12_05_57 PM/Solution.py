// https://leetcode.com/problems/the-latest-time-to-catch-a-bus

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        best = i = 0

        for time in buses:
            cap = capacity
            while i < len(passengers) and passengers[i] <= time and cap > 0:
                i += 1
                cap -= 1

        best = passengers[i - 1]
        passengers = set(passengers)

        if cap > 0:
            best = time
        while best in passengers:
            best -= 1

        return best