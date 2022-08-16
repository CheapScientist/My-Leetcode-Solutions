// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.res = 0
        
        def dfs(node, path):
            if not node: 
                return 
            path = 2*path + node.val
            if not (node.left or node.right):
                self.res += path
            dfs(node.left, path)
            dfs(node.right, path)
        dfs(root, 0)
        return self.res
    