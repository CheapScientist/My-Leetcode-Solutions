// https://leetcode.com/problems/max-points-on-a-line

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if not points: return 0
        # first remove duplicates 
        new = set()
        newP = []
        for x, y in points:
            if (x, y) not in new:
                new.add((x, y))
                newP.append([x, y])
        # then write a helper function to determine A and b:
        
        def helper(x1, y1, x2, y2):
            A = (y1 - y2)/(x1 - x2)
            b = y1 - A*x1
            return A, b
        
        # then have a hash map to store A and b's 
        res = 1
        for i in range(len(newP)):
            memo = {}
            startx, starty = newP[i]
            for x, y in newP[i + 1:]:
                if y == starty: 
                    if str(y) + 'y' not in memo:
                        memo[str(y) + 'y'] = 1
                    else:
                        memo[str(y) + 'y'] += 1
                elif x == startx:
                    if str(x) + 'x' not in memo:
                        memo[str(x) + 'x'] = 1
                    else:
                        memo[str(x) + 'x'] += 1
                else:
                    A, b = helper(startx, starty, x, y)
                    if (A, b) not in memo:
                        memo[(A, b)] = 1
                    else:
                        memo[(A, b)] += 1
            a1 = max(memo.values()) + 1 if memo else 0
            res = max(res, a1)
        return res
                
        
        