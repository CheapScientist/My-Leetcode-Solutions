// https://leetcode.com/problems/subtree-of-another-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        def isSameTree(t1, t2) -> bool:
            if not t1 and not t2:
                return True
            if not t1 and t2:
                return False
            if not t2 and t1:
                return False
            if t2.val != t1.val:
                return False
            ans1 = isSameTree(t1.left, t2.left)
            ans2 = isSameTree(t1.right, t2.right)
            return ans1 and ans2
        
        if not isSameTree(root, subRoot):
            a1 = self.isSubtree(root.left, subRoot)
            a2 = self.isSubtree(root.right, subRoot)
            return a1 or a2
        else:
            return True