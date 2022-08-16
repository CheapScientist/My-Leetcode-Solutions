// https://leetcode.com/problems/merge-two-binary-trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(p, q):
            if not p and not q: return None
            new = TreeNode()
            val = p.val if p else 0
            val += q.val if q else 0
            pleft = p.left if p else None
            pright = p.right if p else None
            qleft = q.left if q else None
            qright = q.right if q else None
            left, right = dfs(pleft, qleft), dfs(pright, qright)
            new.val = val
            new.left, new.right = left, right 
            return new
        return dfs(root1, root2)