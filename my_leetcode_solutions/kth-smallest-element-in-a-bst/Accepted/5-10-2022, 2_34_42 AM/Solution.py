// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return True
        self.ans = []
        
        def inorderDFS(node):
            if not node:
                return 

            inorderDFS(node.left)
            self.ans.append(node.val)
            inorderDFS(node.right)
        inorderDFS(root)
        return self.ans[k - 1]
        