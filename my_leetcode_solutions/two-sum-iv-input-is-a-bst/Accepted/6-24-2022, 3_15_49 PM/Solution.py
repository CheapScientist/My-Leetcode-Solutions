// https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        memo = set()
        def dfs(node):
            if not node: return False
            if k - node.val in memo:
                return True
            memo.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)