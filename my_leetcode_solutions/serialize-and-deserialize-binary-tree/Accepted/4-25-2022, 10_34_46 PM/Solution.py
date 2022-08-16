// https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        ans = []
        q = deque([root])
        ans.append(str(root.val))
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    ans.append(str(cur.left.val))
                    q.append(cur.left)
                else:
                    ans.append('None')
                if cur.right:
                    ans.append(str(cur.right.val))
                    q.append(cur.right)
                else:
                    ans.append('None')
        return ','.join(ans)
                    
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0: return None        
        nodes, q, pos = data.split(","), deque(), 1
        root = TreeNode(int(nodes[0]))
        q.append(root)
        while q:
            n = q.popleft()
            if nodes[pos] != "None":
                n.left = TreeNode(int(nodes[pos]))
                q.append(n.left)
            pos += 1
            if nodes[pos] != "None":
                n.right = TreeNode(int(nodes[pos]))
                q.append(n.right)
            pos += 1
            
        return root
                
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))