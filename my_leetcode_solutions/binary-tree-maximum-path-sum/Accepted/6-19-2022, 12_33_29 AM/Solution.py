// https://leetcode.com/problems/binary-tree-maximum-path-sum

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.maxSF = float('-inf')
        
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            ans = node.val + l + r
            self.maxSF = max(self.maxSF, ans)
            return max(node.val + max(l, r), 0)
        dfs(root)
        return self.maxSF