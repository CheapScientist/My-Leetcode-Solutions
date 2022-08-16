// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        
        def dfs(node):
            if not node: return 
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        dfs(root)
        return ans[k - 1]