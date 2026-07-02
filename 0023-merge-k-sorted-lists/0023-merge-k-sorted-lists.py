# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = [(node.val, idx, node) for idx, node in enumerate(lists) if node]
        heapq.heapify(hq)
        
        dummy = ListNode()
        cur = dummy
        while hq:
            val, idx, node = heapq.heappop(hq)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(hq, (node.next.val, idx, node.next))

        return dummy.next