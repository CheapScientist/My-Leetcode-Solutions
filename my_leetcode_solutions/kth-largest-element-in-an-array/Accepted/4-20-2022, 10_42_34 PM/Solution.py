// https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        maxH = []
        for i in range(k):
            heapq.heappush(maxH, nums[i])
        for i in range(k, len(nums)):
            heapq.heappush(maxH, nums[i])
            heapq.heappop(maxH)
        return heapq.heappop(maxH)