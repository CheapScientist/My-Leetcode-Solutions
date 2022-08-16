// https://leetcode.com/problems/binary-tree-pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node: return False
            left, right = dfs(node.left), dfs(node.right)
            node.left = node.left if left else None
            node.right = node.right if right else None
            return node.val == 1 or left or right
        return root if dfs(root) else None
        