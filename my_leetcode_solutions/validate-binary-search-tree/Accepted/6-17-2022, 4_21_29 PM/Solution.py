// https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def dfs(node, minSoFar, maxSoFar):
            if not node: return True
            if not maxSoFar > node.val > minSoFar:
                return False
            a1 = dfs(node.left, minSoFar, node.val)
            a2 = dfs(node.right, node.val, maxSoFar)
            return a1 and a2
        
        return dfs(root, float('-inf'), float('inf'))
        
        