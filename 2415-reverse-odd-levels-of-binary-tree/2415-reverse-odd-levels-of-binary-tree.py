# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depth = -1
        q = deque([root])
        while q:
            depth += 1
            path = []
            for _ in range(len(q)):
                cur = q.popleft()
                path.append(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if depth % 2 == 0:
                continue
            l, r = 0, len(path) - 1
            while l < r:
                path[l].val, path[r].val = path[r].val, path[l].val
                l += 1
                r -= 1
        return root
