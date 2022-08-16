// https://leetcode.com/problems/path-sum

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        def dfs(node, path):
            if not node:
                return False
            if (not node.left) and (not node.right):
                return path + node.val == targetSum
            path += node.val
            return dfs(node.left, path) or dfs(node.right, path)
        
        return dfs(root, 0)