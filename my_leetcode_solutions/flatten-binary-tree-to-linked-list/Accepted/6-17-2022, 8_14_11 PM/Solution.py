// https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = []
        def dfs(node):
            if not node: return 
            ans.append(node)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        if not ans: ans = [None]
        for i in range(1, len(ans)): 
            ans[i - 1].right = ans[i]
            ans[i - 1].left = None
            