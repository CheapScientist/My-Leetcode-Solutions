// https://leetcode.com/problems/univalued-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.val = None
        self.ans = True
        
        def dfs(node):
            if not node: return 
            if not self.val: 
                self.val = node.val
            else:
                if node.val != self.val:
                    self.ans = False
            dfs(node.left)
            dfs(node.right)
            return 
        dfs(root)
        return self.ans