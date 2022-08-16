// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.path = []
        
        def dfs(node):
            if not node:
                return
            self.path.append(str(node.val))
            if not node.left and not node.right:
                self.ans += int(''.join(self.path))
            dfs(node.left)
            dfs(node.right)
            self.path.pop()
        
        dfs(root)
        return self.ans