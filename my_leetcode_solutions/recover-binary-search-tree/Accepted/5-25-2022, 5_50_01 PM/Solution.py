// https://leetcode.com/problems/recover-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.ans = []
        new = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            self.ans.append(node)
            dfs(node.right)
        dfs(root)
        for i in self.ans:
            new.append(i.val)
        new.sort()
        
        for i, j in enumerate(self.ans):
            j.val = new[i]
        
            
        