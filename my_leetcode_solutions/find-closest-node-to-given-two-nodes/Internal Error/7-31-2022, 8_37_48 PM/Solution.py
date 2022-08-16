// https://leetcode.com/problems/find-closest-node-to-given-two-nodes

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        q1, q2 = deque([node1]), deque([node2])
        v1, v2 = set([node1]), set([node2])
        memo1 = {}
        d1, d2 = 0, 0
        while q1:
            c1 = q1.popleft()
            # if d1: 
            memo1[c1] = d1
            if edges[c1] not in v1 and edges[c1] != -1:
                d1 += 1
                v1.add(edges[c1])
                q1.append(edges[c1])

        ans = float('inf')
        res = -1
        while q2:
            c2 = q2.popleft()
            print(c2)
            if c2 in memo1:
                if max(d2, memo1[c2]) < ans:
                    ans = max(d2, memo1[c2])
                    res = c2
            if edges[c2] not in v2 and edges[c2] != -1:
                d2 += 1
                v2.add(edges[c2])
                q2.append(edges[c2])
                
            
        return res