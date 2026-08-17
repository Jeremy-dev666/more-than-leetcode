# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        # level, order, val
        depth = -1
        # if even level, increasing, odd_val
        # if odd level, decreasing, even_val
        q = deque([root])
        while q:
            depth += 1
            prev = None
            for _ in range(len(q)):
                cur = q.popleft()
                if depth % 2 == 0:
                    if cur.val % 2 == 0 or (prev and cur.val <= prev):
                        return False
                else:
                    if cur.val % 2 != 0 or (prev and cur.val >= prev):
                        return False
                prev = cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return True