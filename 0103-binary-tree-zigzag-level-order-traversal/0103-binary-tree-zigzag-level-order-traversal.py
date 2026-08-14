# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        
        q = deque([root])
        l2r = False
        while q:
            sz = len(q)
            path = []
            l2r = not l2r
            for _ in range(sz):
                cur = q.popleft()
                path.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if not l2r:
                path.reverse()
            ans.append(list(path))

        return ans