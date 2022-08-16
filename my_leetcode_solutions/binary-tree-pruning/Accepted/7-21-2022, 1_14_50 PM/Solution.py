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
            if not node: return None, False
            left, right = dfs(node.left), dfs(node.right)
            node.left = left[0] if left[1] else None
            node.right = right[0] if right[1] else None
            return node, node.val == 1 or left[1] or right[1]
        ans = dfs(root)
        if ans[1]:
            return ans[0]
        else:
            return None
        