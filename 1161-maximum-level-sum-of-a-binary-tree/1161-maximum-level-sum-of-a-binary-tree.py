# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = ans = 0
        total = -inf
        q = deque([root])
        while q:
            sz = len(q)
            sum = 0
            level += 1
            for _ in range(sz):
                cur = q.popleft()
                sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if sum > total:
                total = sum
                ans = level
        return ans