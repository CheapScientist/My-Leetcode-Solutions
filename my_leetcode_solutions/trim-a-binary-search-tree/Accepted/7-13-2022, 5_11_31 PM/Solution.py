// https://leetcode.com/problems/trim-a-binary-search-tree

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        
        def dfs(node):
            if not node: return None
            left, right = dfs(node.left), dfs(node.right)
            if high >= node.val >= low: 
                node.left, node.right = left, right
                return node
            else:
                return left or right
        return dfs(root)