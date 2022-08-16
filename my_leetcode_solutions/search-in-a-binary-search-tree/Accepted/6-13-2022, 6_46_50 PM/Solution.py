// https://leetcode.com/problems/search-in-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return []
        
        q = deque([root])
        while q: 
            cur = q.popleft()
            if not cur: 
                continue
            if cur.val == val: 
                return cur
            elif cur.val < val: 
                q.append(cur.right)
            else:
                q.append(cur.left)
        return None