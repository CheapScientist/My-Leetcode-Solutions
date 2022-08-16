// https://leetcode.com/problems/car-pooling

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        n = len(trips)
        if n == 1:
            return trips[0][0] <= capacity
        minH = [] # add [end, people]
        cur_people = 0
        for i in trips:
            num_people, start, end = i
            while minH and minH[0][0] <= start:
                cur_people -= heapq.heappop(minH)[1]
            cur_people += num_people
            if cur_people > capacity:
                return False
            heapq.heappush(minH, [end, num_people])
        return True