# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ptr = dummy = ListNode(next=head)
        for _ in range(left - 1):
            ptr = ptr.next
        
        prev = None
        cur = ptr.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        ptr.next.next = cur
        ptr.next = prev
        return dummy.next