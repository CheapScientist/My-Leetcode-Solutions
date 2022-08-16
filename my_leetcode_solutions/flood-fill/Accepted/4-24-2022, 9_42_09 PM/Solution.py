// https://leetcode.com/problems/flood-fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image: return []
        rows, cols = len(image), len(image[0])
        oc = image[sr][sc]
        visit = set()
        if oc == newColor: return image
        def dfs(r, c):
            if (r not in range(rows) or 
               c not in range(cols) or 
               image[r][c] != oc or 
               (r, c) in visit):
                return 
            visit.add((r, c))
            image[r][c] = newColor
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        dfs(sr, sc)
        return image