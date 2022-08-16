// https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def dfs(l, r):
            if not l and not r:
                return True
            if l and not r:
                return False
            if r and not l:
                return False
            if r.val != l.val:
                return False
            return dfs(l.left, r.right) and dfs(l.right, r.left)
        return dfs(root.left, root.right)
            
    
        
        