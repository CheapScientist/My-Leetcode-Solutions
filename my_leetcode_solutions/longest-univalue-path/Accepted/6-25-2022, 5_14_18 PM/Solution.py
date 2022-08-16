// https://leetcode.com/problems/longest-univalue-path

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node): 
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow += left
            if node.right and node.right.val == node.val: 
                right_arrow += right
            self.ans = max(self.ans, left_arrow + right_arrow)
            return 1 + max(left_arrow, right_arrow)
        
        dfs(root)
        return self.ans