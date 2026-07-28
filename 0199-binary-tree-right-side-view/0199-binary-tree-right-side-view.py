# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        if root is None:
            return ans

        q = deque([root])
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.popleft()
                if i == sz - 1:
                    ans.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return ans

