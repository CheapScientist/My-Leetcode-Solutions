// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sSplit = s.split()
        if len(pattern) != len(sSplit):
            return False
        counter1 = {}
        for i, j in enumerate(pattern): 
            if j not in counter1:
                counter1[j] = [i]
            else:
                counter1[j].append(i)
        counter2 = {}
        for i, j in enumerate(sSplit):
            counter2[j] = counter2.get(j, []) + [i]
        seen = set()
        for j, i in enumerate(pattern):
            if i not in seen: 
                seen.add(i)
                neighbors1 = counter1[i]
                neighbors2 = counter2[sSplit[j]]
                if neighbors1 != neighbors2:
                    return False
        return True
        
        