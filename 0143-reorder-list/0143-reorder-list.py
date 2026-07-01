# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        # 找到中点(后半段起点)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # second 是后半段起点，反转后半段
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # prev 是后半段链表反转后新起点
        l1, l2 = head, prev
        while l2:
            nxt1 = l1.next
            nxt2 = l2.next
            l1.next = l2
            l2.next = nxt1
            l1 = nxt1
            l2 = nxt2
