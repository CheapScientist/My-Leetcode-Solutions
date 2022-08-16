// https://leetcode.com/problems/find-mode-in-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        memo = {}
        
        def dfs(node):
            if not node: 
                return
            if node.val in memo:
                memo[node.val] += 1
            else:
                memo[node.val] = 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        ans = []
        a = list(memo.values())
        mx = max(a)
        for keys in memo:
            if memo[keys] == mx:
                ans.append(keys)
        return ans
        