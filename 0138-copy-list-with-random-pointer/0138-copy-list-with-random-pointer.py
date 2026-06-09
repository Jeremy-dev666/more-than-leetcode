"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        while cur:
            copy_node = Node(cur.val)
            copy_node.next = cur.next
            cur.next = copy_node
            cur = cur.next.next
        
        cur = head
        while cur:
            copy_node = cur.next
            if cur.random:
                copy_node.random = cur.random.next
            cur = cur.next.next

        cur = head
        new_head = cur.next
        while cur:
            copy_node = cur.next
            cur.next = copy_node.next
            if cur.next:
                copy_node.next = cur.next.next
            cur = cur.next
        return new_head
        
