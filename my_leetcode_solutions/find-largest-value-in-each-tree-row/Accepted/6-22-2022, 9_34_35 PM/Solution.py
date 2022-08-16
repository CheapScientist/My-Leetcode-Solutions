// https://leetcode.com/problems/find-largest-value-in-each-tree-row

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(node, height):
            if not node: return 
            if len(res) - 1 < height: 
                res.append(node.val)
            else:
                res[height] = max(res[height], node.val)
            dfs(node.left, height + 1)
            dfs(node.right, height + 1)
        dfs(root, 0)
        return res
            