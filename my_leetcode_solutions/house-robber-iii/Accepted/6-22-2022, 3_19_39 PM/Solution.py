// https://leetcode.com/problems/house-robber-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        memo = {}
        def dfs(node, canRob):
            if not node: return 0
            if (node, canRob) in memo: return memo[(node, canRob)]
            if canRob: 
                # decision 1: not rob this one
                a1 = dfs(node.left, True) + dfs(node.right, True)
                a2 = node.val + dfs(node.left, False) + dfs(node.right, False)
                memo[(node, canRob)] = max(a1, a2)
                return max(a1, a2)
            else:
                a3 = dfs(node.left, True) + dfs(node.right, True)
                memo[(node, canRob)] = a3
                return a3
        return dfs(root, True)