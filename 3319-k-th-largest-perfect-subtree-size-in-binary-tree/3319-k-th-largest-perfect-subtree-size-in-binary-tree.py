# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        def dfs(node):
            if node is None:
                return (True, 0)

            l_flag, l_size = dfs(node.left)
            r_flag, r_size = dfs(node.right)

            if l_flag and r_flag and l_size == r_size:
                size = l_size + r_size + 1
                if len(heap) < k:
                    heapq.heappush(heap, size)
                elif size > heap[0]:
                    heapq.heapreplace(heap, size)
                return (True, size)
            else:
                return (False, -1)

        dfs(root)
        return heap[0] if len(heap) == k else -1
            