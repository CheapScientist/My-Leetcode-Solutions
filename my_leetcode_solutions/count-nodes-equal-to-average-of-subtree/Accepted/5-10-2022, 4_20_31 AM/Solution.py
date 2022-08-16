// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.res = 0
        def dfs(node):
            if not node: return 0, 0 # val, number of nodes
            lv, ln = dfs(node.left)
            rv, rn = dfs(node.right)
            val = node.val + lv + rv
            numNodes = 1 + ln + rn
            if node.val == val//numNodes:
                self.res += 1
            return val, numNodes
        dfs(root)
        return self.res