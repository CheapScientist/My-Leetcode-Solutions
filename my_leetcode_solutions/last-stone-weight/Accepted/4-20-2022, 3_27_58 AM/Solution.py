// https://leetcode.com/problems/last-stone-weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxH = []
        l = len(stones)
        for i in stones:
            heapq.heappush(maxH, -i)
        while l > 1:
            stone1 = -1 * heapq.heappop(maxH)
            stone2 = -1 * heapq.heappop(maxH)
            if stone1 == stone2:
                l -= 2
                heapq.heappush(maxH, 0)
            else:
                l -= 1
                heapq.heappush(maxH, -abs(stone1 - stone2))

        return -maxH[0]