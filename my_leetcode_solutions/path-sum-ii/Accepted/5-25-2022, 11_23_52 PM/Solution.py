// https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []
        self.path = []
        if not root: return []
        
        def dfs(node, path):
            if not node: 
                return 
            self.path.append(node.val)
            path += node.val
            if not node.left and not node.right:
                if path == targetSum:
                    self.res.append(self.path[:])
            dfs(node.left, path)
            dfs(node.right, path)
            self.path.pop()
        
        dfs(root, 0)
        return self.res
        