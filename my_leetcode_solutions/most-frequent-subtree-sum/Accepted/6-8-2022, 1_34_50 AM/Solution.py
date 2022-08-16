// https://leetcode.com/problems/most-frequent-subtree-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        memo = {}
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            ans = left + right + node.val
            memo[ans] = memo.get(ans, 0) + 1
            return ans
        
        dfs(root)
        val = list(memo.values())
        mx = max(val)
        ans = []
        for keys in memo:
            if memo[keys] == mx:
                ans.append(keys)
        return ans