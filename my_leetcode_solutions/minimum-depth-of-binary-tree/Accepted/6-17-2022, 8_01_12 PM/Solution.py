// https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.ans = float('inf')
        def dfs(node, length): 
            if not node: return 
            if not node.left and not node.right: 
                self.ans = min(self.ans, length)
                return 
            dfs(node.left, length + 1)
            dfs(node.right, length + 1)
        dfs(root, 1)
        return self.ans
            