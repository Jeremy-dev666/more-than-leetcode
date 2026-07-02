# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        cnt = 0     # 统计未反转节点的个数
        while cur:
            cur = cur.next
            cnt += 1
        
        # K个一组处理
        ptr = dummy = ListNode(0, head)
        cur = head
        prev = None
        while cnt >= k:
            cnt -= k
            # 反转k个节点
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            nxt = ptr.next
            nxt.next = cur
            ptr.next = prev
            ptr = nxt

        return dummy.next
