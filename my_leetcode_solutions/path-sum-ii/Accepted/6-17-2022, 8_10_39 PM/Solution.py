// https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        res = []
        
        def dfs(node, build, sm):
            if not node: 
                return 
            if not node.left and not node.right: 
                if sm + node.val == targetSum:
                    res.append(build + [node.val])

            dfs(node.left, build + [node.val], sm + node.val)
            dfs(node.right, build + [node.val], sm + node.val)
            return 
        dfs(root, [], 0)
        return res