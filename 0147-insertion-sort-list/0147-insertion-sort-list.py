# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = head
        
        while cur:
            prev = dummy
            nxt = cur.next
            while prev.next and prev.next.val <= cur.val:
                prev = prev.next
            # cur 插入到相应位置
            cur.next = prev.next
            prev.next = cur
            cur = nxt

        return dummy.next
