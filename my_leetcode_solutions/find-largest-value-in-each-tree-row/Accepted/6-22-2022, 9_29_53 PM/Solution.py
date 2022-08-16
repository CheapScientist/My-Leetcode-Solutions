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
        
        q = deque([root])
        while q:
            temp = float('-inf')
            for i in range(len(q)):
                cur = q.popleft()
                if not cur: 
                    continue
                temp = max(temp, cur.val)
                q.append(cur.left)
                q.append(cur.right)
            if temp != float('-inf'):
                res.append(temp)
        return res
            