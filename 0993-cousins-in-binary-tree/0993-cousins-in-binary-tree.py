# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(root, None)])
        while q:
            found = {}
            for _ in range(len(q)):
                cur, cur_prnt = q.popleft()
                if cur.val == x or cur.val == y:
                    found[cur.val] = cur_prnt
                if cur.left:
                    q.append((cur.left, cur.val))
                if cur.right:
                    q.append((cur.right, cur.val))
            
            if len(found) == 2:
                return found[x] != found[y]
            elif len(found) == 1:
                return False
        return False
