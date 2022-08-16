// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_memo = {}
        def dfs1(node):
            if not node: return 
            if node.left: 
                parent_memo[node.left] = node
            if node.right:
                parent_memo[node.right] = node
            dfs1(node.left)
            dfs1(node.right)
            return 
        dfs1(root)
        ans = []
        visit = set()
        
        def dfs2(node, distance):
            if not node or node in visit: return 
            visit.add(node)
            if distance == k: 
                ans.append(node.val)
            if node in parent_memo:
                dfs2(parent_memo[node], distance + 1)
            if node.left:
                dfs2(node.left, distance + 1)
            if node.right:
                dfs2(node.right, distance + 1)
            return 
        dfs2(target, 0)
        return ans
    
    
    