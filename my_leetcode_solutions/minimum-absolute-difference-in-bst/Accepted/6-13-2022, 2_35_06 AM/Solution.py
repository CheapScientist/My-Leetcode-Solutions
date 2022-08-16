// https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = []
        
        def dfs(node): 
            if not node: return 
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        if len(res) == 1: 
            return -1 
        ans = float('inf')
        for i in range(1, len(res)): 
            diff = res[i] - res[i - 1]
            ans = min(ans, diff)
        return ans