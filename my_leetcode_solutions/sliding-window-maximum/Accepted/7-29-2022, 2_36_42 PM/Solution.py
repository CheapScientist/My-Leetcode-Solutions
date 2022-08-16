// https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= k: return [max(nums)]
        maxHeap = [[-nums[idx], idx] for idx in range(k - 1)]
        heapq.heapify(maxHeap)
        ans = []
        for i in range(k-1, n):
            heapq.heappush(maxHeap, [-nums[i], i])
            while maxHeap and maxHeap[0][1] <= i - k:
                heapq.heappop(maxHeap)
            ans.append(-maxHeap[0][0])
        return ans