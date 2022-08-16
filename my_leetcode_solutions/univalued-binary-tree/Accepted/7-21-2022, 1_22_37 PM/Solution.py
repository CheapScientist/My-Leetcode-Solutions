// https://leetcode.com/problems/univalued-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node: return True
            left, right = dfs(node.left), dfs(node.right)
            a1 = node.left.val == node.val if node.left else True
            a2 = node.right.val == node.val if node.right else True
            return left and right and a1 and a2
        
        return dfs(root)