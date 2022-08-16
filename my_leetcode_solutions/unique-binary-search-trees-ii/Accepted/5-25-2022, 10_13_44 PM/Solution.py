// https://leetcode.com/problems/unique-binary-search-trees-ii

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def dfs(l, r):
            if l > r:
                return [None]
            
            temp = []
            for i in range(l, r + 1):
                left = dfs(l, i - 1)
                right = dfs(i + 1, r )
                for le in left:
                    for ri in right:
                        root = TreeNode(i)
                        root.left = le
                        root.right = ri
                        temp.append(root)
            return temp
        return dfs(1, n)