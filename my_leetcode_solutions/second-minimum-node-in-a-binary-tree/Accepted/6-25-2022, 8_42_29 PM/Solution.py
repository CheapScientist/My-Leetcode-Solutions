// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = []
        
        def dfs(node):
            if not node: return 
            ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        res = list(set(ans))

        if len(res) > 1: 
            return sorted(res)[1]
        else:
            return -1