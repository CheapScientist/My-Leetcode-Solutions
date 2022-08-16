// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        def dfs(node):
            if not node: return None
            if node.val == p.val or node.val == q.val:
                return node
            elif node.val < min(p.val, q.val): 
                return dfs(node.right)
            elif node.val > max(p.val, q.val):
                return dfs(node.left)
            else:
                return node
        
        return dfs(root)