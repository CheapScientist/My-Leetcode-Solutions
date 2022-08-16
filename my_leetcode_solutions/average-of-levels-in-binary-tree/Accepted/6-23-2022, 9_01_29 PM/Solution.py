// https://leetcode.com/problems/average-of-levels-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])
        while q: 
            nodes = 0
            total = 0
            found = False
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur:
                    continue
                found = True
                nodes += 1
                total += cur.val
                q.append(cur.left)
                q.append(cur.right)
            if found: 
                ans.append(total/nodes)
        return ans