// https://leetcode.com/problems/smallest-string-starting-from-leaf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = []
        if not root: return ''
        
        def dfs(node, path):
            if node:
                if not node.left and not node.right:
                    res.append((path+chr(node.val + ord('a')))[::-1])
                dfs(node.left, path+chr(node.val + ord('a')))
                dfs(node.right,path+chr(node.val + ord('a')))

        dfs(root, '')
        res.sort()
        return res[0]
        