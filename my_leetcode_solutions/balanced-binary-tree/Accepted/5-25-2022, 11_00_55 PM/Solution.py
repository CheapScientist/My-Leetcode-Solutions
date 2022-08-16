// https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def dfs(node):
            if not node:
                return [True, 0]
            leftRes = dfs(node.left)
            rightRes = dfs(node.right)
            res = leftRes[0] and rightRes[0] and (abs(leftRes[1] - rightRes[1]) <= 1)
            return [res, 1 + max(leftRes[1], rightRes[1])]
        
        return dfs(root)[0]
        
        