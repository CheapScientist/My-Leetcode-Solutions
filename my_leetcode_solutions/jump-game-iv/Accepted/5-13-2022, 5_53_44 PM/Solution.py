// https://leetcode.com/problems/jump-game-iv

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]
        q = deque([0]) # store current layers
        visit = {0}
        step = 0

        # when current layer exists
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur == n - 1:
                    return step
                for nei in graph[arr[cur]] + [min(cur + 1, len(arr) - 1), max(cur - 1, 0)]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
                graph[arr[cur]].clear()
            step += 1
        return -1