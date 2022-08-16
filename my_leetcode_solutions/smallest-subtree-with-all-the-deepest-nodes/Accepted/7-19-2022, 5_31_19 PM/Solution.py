// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.deepest_nodes = []
        self.depth = 0
        memo = {root: None}
        
        def dfs(node, depth):
            if not node: return
            if node.left:
                memo[node.left] = node
            if node.right:
                memo[node.right] = node
            if depth > self.depth:
                self.deepest_nodes = [node]
                self.depth = depth
            if depth == self.depth:
                self.deepest_nodes.append(node)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
            return 
        
        dfs(root, 0)
        if len(self.deepest_nodes) == 1:
            return self.deepest_nodes[0]
        
        def dfs2(node_list):
            n = len(node_list)
            if all(node_list[i] == node_list[i + 1] for i in range(n - 1)):
                return node_list[0]
            return dfs2([memo[node_list[i]] for i in range(n)])
        return dfs2(self.deepest_nodes)