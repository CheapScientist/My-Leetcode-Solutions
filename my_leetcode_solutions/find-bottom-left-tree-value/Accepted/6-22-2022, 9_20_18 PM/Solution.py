// https://leetcode.com/problems/find-bottom-left-tree-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.ans = -1
        self.height = -1
        if not root: return None
        
        def dfs(node, height):
            if not node: return 
            if height >= self.height: 
                self.height = height
                self.ans = node.val
            dfs(node.right, height + 1)
            dfs(node.left, height + 1)
        
        dfs(root, 0)
        return self.ans