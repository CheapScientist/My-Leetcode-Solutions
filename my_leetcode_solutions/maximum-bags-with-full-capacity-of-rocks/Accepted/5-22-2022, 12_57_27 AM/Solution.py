// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        res = 0
        new = []
        for cap, rock in zip(capacity, rocks):
            if cap > rock:
                new.append(cap - rock)
            elif cap == rock:
                res += 1
            else:
                continue
        new.sort()
        i = 0
        while i < len(new):
            if additionalRocks >= new[i]:
                res += 1
                additionalRocks -= new[i]
                i += 1
            else:
                break
        return res
            
        
            
        
        