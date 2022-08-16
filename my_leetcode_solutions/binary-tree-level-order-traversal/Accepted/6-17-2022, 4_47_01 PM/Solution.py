// https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root: return []
        res = []
        q = deque([root])
        while q:
            res.append([])
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur:
                    continue
                res[-1].append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            if not res[-1]: 
                res.pop()
        return res
                