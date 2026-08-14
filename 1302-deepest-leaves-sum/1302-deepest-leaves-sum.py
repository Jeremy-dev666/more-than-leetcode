# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        depth, max_depth = 1, 0
        q = deque([root])
        while q:
            total = 0
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left is None and cur.right is None:
                    total += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if depth > max_depth:
                ans = total
            depth += 1

        return ans
            