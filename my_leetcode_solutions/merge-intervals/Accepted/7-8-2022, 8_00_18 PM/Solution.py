// https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, A: List[List[int]]) -> List[List[int]]:
        if len(A) == 1: return A
        A.sort(key = lambda x: x[0])
        ans = [A[0]]
        
        for i in range(1, len(A)): 
            prevstart, prevend = ans[-1]
            start, end = A[i]
            if start > prevend: 
                ans.append(A[i])
            elif end <= prevend: 
                continue
            else:
                ans.pop()
                ans.append([prevstart, max(end, prevend)])
        return ans