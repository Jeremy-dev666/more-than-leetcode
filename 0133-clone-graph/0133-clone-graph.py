"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node

        q = deque([node])
        # key: original node | val: clone node
        has_cloned = {node: Node(node.val)}

        while q:
            cur = q.popleft()
            for nb in cur.neighbors:
                if nb not in has_cloned:
                    has_cloned[nb] = Node(nb.val)
                    q.append(nb)
                has_cloned[cur].neighbors.append(has_cloned[nb])

        return has_cloned[node]