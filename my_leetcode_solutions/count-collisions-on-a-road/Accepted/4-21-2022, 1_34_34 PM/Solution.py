// https://leetcode.com/problems/count-collisions-on-a-road

class Solution:
    def countCollisions(self, D: str) -> int:
        return sum(d!='S' for d in D.lstrip('L').rstrip('R'))