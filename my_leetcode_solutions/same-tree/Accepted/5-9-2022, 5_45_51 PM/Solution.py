// https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not q and p) or (not p and q):
            return False
        if p and q and p.val != q.val:
            return False
        if p and q and p.val == q.val:
            a1 = self.isSameTree(p.left, q.left)
            a2 = self.isSameTree(p.right, q.right)
            return a1 and a2
        if not p and not q:
            return True
        