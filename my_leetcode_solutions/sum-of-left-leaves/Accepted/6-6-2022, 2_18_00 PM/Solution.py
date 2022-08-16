// https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        def dfs(node):
            if not node:
                return 0
            if node.left and not node.left.left and not node.left.right:
                ans = node.left.val
            else:
                ans = 0
            a1 = dfs(node.left)
            a2 = dfs(node.right)
            return ans+a1+a2
        
        return dfs(root)