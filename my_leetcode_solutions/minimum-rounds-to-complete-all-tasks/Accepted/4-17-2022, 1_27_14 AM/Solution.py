// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        if not tasks: return -1
        hashTable = {}
        ans = 0
        for i in tasks:
            if i not in hashTable:
                hashTable[i] = 1
            else:
                hashTable[i] += 1
        for j in hashTable.values():
            if j == 1:
                return -1
            if j % 3 == 1 or j % 3 == 2:
                ans += j//3 + 1
            else:
                ans += j/3
        
        return int(ans)
        