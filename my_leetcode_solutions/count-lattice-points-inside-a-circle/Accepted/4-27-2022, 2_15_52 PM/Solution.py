// https://leetcode.com/problems/count-lattice-points-inside-a-circle

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        lookup = {}
        ansSet = set()
        for x, y, r in circles:
            for xx in range(x - r, x + r + 1):
                for yy in range(y - r, y + r + 1):
                    if (xx, yy, x, y, r) not in lookup:  
                        a1 = ((xx - x)**2 + (yy - y)**2 <= r**2)
                        lookup[(xx, yy, x, y, r)] = a1
                        if a1: 
                            ansSet.add((xx, yy))
                            

        return len(ansSet)