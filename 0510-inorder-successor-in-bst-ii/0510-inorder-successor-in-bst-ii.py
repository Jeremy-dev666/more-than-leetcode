"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        def findroot(node):
            cur = node
            while cur.parent:
                cur = cur.parent
            return cur
        root = findroot(node)

        self.ans = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.ans.append(node)
            dfs(node.right)
        dfs(root)

        for i, nd in enumerate(self.ans):
            if i < len(self.ans) - 1 and nd == node:
                return self.ans[i + 1]
        return None
        

        