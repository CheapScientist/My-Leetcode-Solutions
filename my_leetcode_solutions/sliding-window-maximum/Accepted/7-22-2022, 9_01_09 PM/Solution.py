// https://leetcode.com/problems/sliding-window-maximum

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = [] # we gonna push like [val, idx]
        l, r, n = 0, k - 1, len(nums)
        for i in range(l, r + 1):
            heapq.heappush(maxHeap, [-nums[i], i])
        ans = [-maxHeap[0][0]]
        for i in range(k, n):
            heapq.heappush(maxHeap, [-nums[i], i])
            while maxHeap[0][1] <= i - k:
                heapq.heappop(maxHeap)
            ans.append(-maxHeap[0][0])

        return ans
        