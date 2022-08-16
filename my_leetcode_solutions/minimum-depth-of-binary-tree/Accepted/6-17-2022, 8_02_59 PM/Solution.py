// https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        if not root: return 0
        length = 1
        while q: 
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur: 
                    continue
                if not cur.left and not cur.right: 
                    return length
                q.append(cur.left)
                q.append(cur.right)
                    
            length += 1
        return -1