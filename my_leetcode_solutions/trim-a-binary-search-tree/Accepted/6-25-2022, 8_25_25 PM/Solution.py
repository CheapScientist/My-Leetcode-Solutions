// https://leetcode.com/problems/trim-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        
        def dfs(node):
            if not node: return None
            newNode = TreeNode()
            left, right = dfs(node.left), dfs(node.right)
            if high >= node.val >= low: 
                newNode.val = node.val
                newNode.left, newNode.right = left, right
                return newNode
            else:
                newNode = left or right
                return newNode
        return dfs(root)
            