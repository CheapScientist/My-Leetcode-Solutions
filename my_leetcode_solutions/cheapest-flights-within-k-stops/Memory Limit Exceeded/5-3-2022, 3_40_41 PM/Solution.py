// https://leetcode.com/problems/cheapest-flights-within-k-stops

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int):
        adj = {i:[] for i in range(n)}
        for fr, to, price in flights:
            adj[fr].append([price, to])
        # return adj
        possiblePrices = []
        # visit = set()
        q = deque()
        q.append([0, src])
        stops = 0

        while stops <= k + 1:
            for i in range(len(q)):
                curPrice, curPlace = q.popleft()
                if curPlace == dst:
                    possiblePrices.append(curPrice)
                    continue
                # if curPlace not in visit:
                #     visit.add(curPlace)
                for neiPrice, nei in adj[curPlace]:
                    q.append([neiPrice + curPrice, nei])
            stops += 1
        return min(possiblePrices) if possiblePrices else -1