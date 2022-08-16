// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.depth = 0
        self.memo = set()
        
        def dfs(node, depth):
            if not node: return
            if depth > self.depth: 
                self.memo = set()
                self.memo.add(node)
                self.depth = depth
            elif depth == self.depth:
                self.memo.add(node)
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            return 
        dfs(root, 0)
        
        def dfs2(node):
            if not node: return None 
            ans = None
            if node in self.memo: 
                ans = node
            left, right = dfs2(node.left), dfs2(node.right)
            if left and right: 
                return node
            else:
                return ans or left or right
        
        return dfs2(root)
            
            
                
                
                
        