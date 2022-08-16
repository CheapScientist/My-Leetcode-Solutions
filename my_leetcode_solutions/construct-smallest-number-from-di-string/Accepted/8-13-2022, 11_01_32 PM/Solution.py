// https://leetcode.com/problems/construct-smallest-number-from-di-string

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # pattern = "IIIDIDDD"
        # 1 2 3 5 4 7 6 
        n = len(pattern)
        self.ans = []
        
        
        def dfs(i, prev):
            if i == n:
                self.ans.append(''.join(path))
                return 
            cur = pattern[i]
            if cur == 'I':
                for j in range(prev + 1, 10):
                    if j not in seen:
                        seen.add(j)
                        path.append(str(j))
                        dfs(i + 1, j)
                        seen.remove(j)
                        path.pop()
            else:
                for j in range(prev - 1, 0, -1):
                    if j not in seen:
                        seen.add(j)
                        path.append(str(j))
                        dfs(i + 1, j)
                        seen.remove(j)
                        path.pop()
            return 
                
            
        for i in range(1, 10):
            path = [str(i)]
            seen = set([i])
            dfs(0, i)
        return min(sorted(self.ans))