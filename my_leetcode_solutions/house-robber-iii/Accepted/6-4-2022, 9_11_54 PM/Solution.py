// https://leetcode.com/problems/house-robber-iii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        
        def dfs(node, canSteal):
            if (node, canSteal) in memo:
                return memo[(node, canSteal)]
            if not node: return 0
            # two cases: 1. can steal
            if canSteal:
                # inside this we have two decisions: steal or not steal
                # case steal: 
                ans1 = node.val + dfs(node.left, False) + dfs(node.right, False)
                # ans = max(ans, ans1)
                # # case not steal:
                ans2 = dfs(node.left, True) + dfs(node.right, True)
                ans = max(ans1, ans2)
            else:
                # if we cannot steal 
                ans3 = dfs(node.left, True) + dfs(node.right, True)
                ans = ans3
            memo[(node, canSteal)] = ans
            return ans
        
        return dfs(root, True)
        
        