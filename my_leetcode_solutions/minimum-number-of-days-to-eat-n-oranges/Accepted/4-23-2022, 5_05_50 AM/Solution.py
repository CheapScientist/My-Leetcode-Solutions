// https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges

class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        q=deque()
        q.append(n)
        steps=0
        visited=set()
        
        while(len(q)):
            l=len(q)
            
            for _ in range(l):
                x=q.popleft()
                if x%3==0 and x//3 not in visited:
                    q.append(x//3)
                    visited.add(x//3)
                if x%2==0 and x//2 not in visited:
                    visited.add(x//2)
                    q.append(x//2)
                if x-1 not in visited:
                    visited.add(x-1)
                    q.append(x-1)
                if x-1==0:
                    return steps + 1
            steps+=1