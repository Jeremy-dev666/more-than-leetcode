# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        cur_depth = 0
        q = deque([root])
        while q:
            cur_depth += 1

            for _ in range(len(q)):
                cur = q.popleft()
                if cur_depth + 1 == depth:
                    left = cur.left
                    right = cur.right
                    new_left, new_right = TreeNode(val), TreeNode(val)
                    cur.left = new_left
                    cur.right = new_right
                    new_left.left = left
                    new_right.right = right
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return root
                    