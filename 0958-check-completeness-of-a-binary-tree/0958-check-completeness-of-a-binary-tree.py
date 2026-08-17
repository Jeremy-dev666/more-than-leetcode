# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """同层：null节点之后如果还有非空节点就返回False"""
        q = deque([root])
        seen_null = False
        while q:
            node = q.popleft()
            if node is None:
                seen_null = True
                continue
            if seen_null:
                return False

            q.append(node.left)
            q.append(node.right)
        return True
