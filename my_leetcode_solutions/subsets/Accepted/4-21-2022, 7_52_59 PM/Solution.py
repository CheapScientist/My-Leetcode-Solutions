// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: list[int]):
        temp = deque()
        temp.append([])
        x = deque(nums)
        while x:
            cur = x.popleft()
            for i in range(len(temp)):
                y = temp.popleft()
                temp.append(y + [cur])
                temp.append(y)
        return list(temp)