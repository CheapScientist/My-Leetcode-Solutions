// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        memo = {}
        for i, j in enumerate(inorder):
            memo[j] = i
        self.i = 0
        
        def dfs(l, r):
        
            if l > r: 
                return None
            root = TreeNode(preorder[self.i])
            root_index = memo[root.val]
            self.i += 1
            root.left = dfs(l, root_index - 1)
            root.right = dfs(root_index + 1, r)
            return root
        return dfs(0, n - 1)