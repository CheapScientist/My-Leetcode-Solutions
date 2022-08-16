// https://leetcode.com/problems/count-good-nodes-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0

        def dfs(node, prevVal):
            if not node: 
                return 
            if node.val >= prevVal:
                self.res += 1
            dfs(node.left, max(node.val, prevVal))
            dfs(node.right, max(node.val, prevVal))
        
        dfs(root, root.val)
        return self.res
        