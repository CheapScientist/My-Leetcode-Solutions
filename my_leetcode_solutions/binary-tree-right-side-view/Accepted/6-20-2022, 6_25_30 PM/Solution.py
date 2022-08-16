// https://leetcode.com/problems/binary-tree-right-side-view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        ans = []
        while q: 
            temp = []
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur:
                    continue
                q.append(cur.left)
                q.append(cur.right)
                temp.append(cur.val)
            if temp: 
                ans.append(temp[-1])
        return ans