// https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        def dfs1(node):
            if not node: return 0
            
            return 1 + dfs1(node.left)
        
        def dfs2(node):
            if not node: return 0
            
            return 1 + dfs2(node.right)
        
        def main(node):
            if not node: return 0
            left = dfs1(node)
            right = dfs2(node)
            if left == right: 
                return (2**left - 1)
            else:
                return main(node.left) + main(node.right) + 1
        return main(root)